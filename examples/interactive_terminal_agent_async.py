#!/usr/bin/env python3
"""
OpenCode Interactive Terminal Agent Example (Async Version)

这个示例展示如何使用 opencode-sdk 的异步API构建一个终端交互式 AI Agent,实现:
- 通过终端输入问题
- 实时流式展示 AI 回复
- 显示工具调用和执行状态
- 维护会话中的对话历史
- 优雅地处理错误
"""

import sys
import asyncio
from typing import Optional

from opencode_sdk import AsyncOpencodeSDK, omit, id_ascending
from opencode_sdk.types.event_list_response import EventListResponse
from opencode_sdk.types.session import message_create_params

try:
    from rich.console import Console
    from rich.panel import Panel

    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    print("提示: 安装 rich 库可以获得更好的显示效果: pip install rich", file=sys.stderr)


class InteractiveTerminalAgent:
    """
    使用 OpenCode SDK 的异步交互式终端 Agent。

    这个 Agent 可以:
    1. 接收用户的命令行输入
    2. 通过 SSE 实时接收和显示 AI 的回复
    3. 展示工具调用和执行状态
    4. 支持多轮对话
    """

    def __init__(self, base_url: str):
        """
        初始化 Agent。

        Args:
            base_url: OpenCode 服务器地址
        """
        # 创建 SDK 异步客户端
        self.client = AsyncOpencodeSDK(base_url=base_url)

        # 初始化 Rich Console (如果可用)
        if HAS_RICH:
            self.console = Console()
        else:
            self.console = None

        # 会话和配置
        self.session_id: Optional[str] = None
        self.provider_id: Optional[str] = None
        self.model_id: Optional[str] = None
        self.agent_name: Optional[str] = None

        # 用于跟踪当前消息的状态
        self.current_message_id: Optional[str] = None
        self.current_text_parts: dict = {}
        self.current_tool_parts: dict = {}
        self.message_completed = False

        # 用于控制事件循环
        self.event_task: Optional[asyncio.Task] = None
        self.stop_event = asyncio.Event()

    def _print(self, text: str = '\n', **kwargs):
        """统一的打印方法,支持 Rich 和普通输出。"""
        # 从 kwargs 中提取 file 参数（Rich 不支持 file 参数）
        file = kwargs.pop('file', None)

        if self.console:
            # Rich Console 使用 stderr 参数而不是 file
            if file == sys.stderr:
                self.console.print(text, **kwargs, file=sys.stderr)
            else:
                self.console.print(text, **kwargs)
        else:
            if file:
                print(text, file=file, **kwargs)
            else:
                print(text, **kwargs)

    def _print_panel(self, content: str, title: str = "", border_style: str = ""):
        """显示面板。"""
        if self.console:
            self.console.print(Panel(content, title=title, border_style=border_style))
        else:
            print(f"\n{'=' * 60}")
            if title:
                print(f"{title}")
                print('-' * 60)
            print(content)
            print('=' * 60)

    async def initialize(self):
        """初始化 Agent:获取配置、创建会话、订阅事件。"""
        self._print(f"[cyan]正在连接到 OpenCode 服务器...[/cyan]")

        try:
            # 1. 获取当前项目信息
            project = await self.client.project.retrieve_current()
            self._print(f"[green]已连接到项目:[/green] {project.worktree}")

            # 2. 获取可用的 agents
            agents = await self.client.agent.list()
            if not agents:
                raise RuntimeError("没有可用的 agent")

            # 选择第一个 agent
            self.agent_name = agents[0].name
            self._print(f"[green]使用 Agent:[/green] {self.agent_name}")

            # 3. 获取 providers 和 models
            providers_resp = await self.client.config.list_providers()
            providers = providers_resp.providers

            if not providers:
                raise RuntimeError("没有可用的 provider")

            self.provider_id = 'anthropic'
            self.model_id = 'claude-sonnet-4-5-20250929'

            self._print(f"[green]使用模型:[/green] {self.provider_id} - {self.model_id}")

            # 4. 创建 session
            session = await self.client.session.create(title="Terminal Chat Session")
            self.session_id = session.id
            self._print(f"[green]会话已创建:[/green] {self.session_id}")

            # 5. 订阅 SSE 事件流
            await self._subscribe_events()

            self._print("\n[bold green]初始化完成![/bold green]\n")

        except Exception as e:
            self._print(f"[bold red]初始化失败:[/bold red] {e}")
            raise

    async def _subscribe_events(self):
        """订阅 SSE 事件流。"""

        async def event_loop():
            """在后台任务中处理 SSE 事件。"""
            try:
                # 使用 SDK 的 event.list() 获取事件流
                event_stream = await self.client.event.list()

                async for event in event_stream:
                    if self.stop_event.is_set():
                        break

                    # 处理事件
                    self._handle_event(event)

            except Exception as e:
                if not self.stop_event.is_set():
                    print(f"\n事件流错误: {e}", file=sys.stderr)

        # 在后台任务中启动事件循环
        self.event_task = asyncio.create_task(event_loop())

        # 等待一小段时间,确保连接建立
        await asyncio.sleep(0.5)

    def _handle_event(self, event: EventListResponse):
        """处理从 SSE 接收到的事件。"""
        # 事件类型通过 discriminator 'type' 区分
        event_data = event.model_dump()
        event_type = event_data.get('type')
        properties = event_data.get('properties', {})

        if event_type == 'message.updated':
            self._handle_message_update(properties.get('info', {}))
        elif event_type == 'message.part.updated':
            self._handle_part_update(properties.get('part', {}))
        elif event_type == 'session.error':
            self._handle_error(properties)

    def _handle_message_update(self, info: dict):
        """处理消息更新事件。"""
        if info.get('role') != 'assistant':
            return

        message_id = info.get('id')
        time_info = info.get('time', {})

        # 检查消息是否完成
        if time_info.get('completed', 0):
            self.current_message_id = None
            self.message_completed = True
        else:
            # 消息开始
            self.current_message_id = message_id
            self.message_completed = False
            self.current_text_parts = {}
            self.current_tool_parts = {}

    def _handle_part_update(self, part: dict):
        """处理消息部分更新事件。"""
        part_type = part.get('type')

        if part_type == 'text':
            self._handle_text_part(part)
        elif part_type == 'tool':
            self._handle_tool_part(part)
        elif part_type == 'reasoning':
            self._handle_reasoning_part(part)

    def _handle_text_part(self, part: dict):
        """处理文本部分的流式更新。"""
        part_id = part.get('id')
        text = part.get('text', '')

        # 存储累积的文本
        old_text = self.current_text_parts.get(part_id, '')
        self.current_text_parts[part_id] = text

        # 只打印新增的文本 (delta)
        if text.startswith(old_text):
            delta = text[len(old_text):]
            if delta:
                # 不换行,流式输出
                if self.console:
                    self.console.print(delta, end='')
                else:
                    print(delta, end='', flush=True)

    def _handle_tool_part(self, part: dict):
        """处理工具调用部分的更新。"""
        part_id = part.get('id')
        tool_name = part.get('tool')
        state = part.get('state', {})
        status = state.get('status')

        # 存储工具状态
        self.current_tool_parts[part_id] = part

        if status == 'running':
            tool_input = state.get('input', {})
            title = state.get('title', f'运行 {tool_name}')
            self._print(f"\n\n[bold yellow]🔧 {title}[/bold yellow]")

            # 显示工具输入 (简化)
            if tool_input:
                import json
                input_str = json.dumps(tool_input, ensure_ascii=False, indent=2)
                if len(input_str) > 200:
                    input_str = input_str[:200] + '...'
                self._print(f"[dim]{input_str}[/dim]")

        elif status == 'completed':
            output = state.get('output', '')
            title = state.get('title', f'{tool_name} 完成')
            self._print(f"\n[green]✓ {title}[/green]")

            # 显示截断的输出
            if len(output) > 300:
                self._print(f"[dim]{output[:300]}...[/dim]")
            elif output:
                self._print(f"[dim]{output}[/dim]")

            self._print()  # 添加空行

        elif status == 'error':
            error = state.get('error', 'Unknown error')
            self._print(f"\n[bold red]✗ {tool_name} 失败:[/bold red] {error}\n")

    def _handle_reasoning_part(self, part: dict):
        """处理推理部分的更新。"""
        text = part.get('text', '')
        if text:
            self._print(f"\n[italic dim]推理: {text}[/italic dim]\n")

    def _handle_error(self, properties: dict):
        """处理会话错误事件。"""
        error = properties.get('error', {})
        error_name = error.get('name', 'Unknown error')
        error_data = error.get('data', {})

        self._print(f"\n[bold red]错误:[/bold red] {error_name}")
        if error_data:
            import json
            self._print(f"[red]{json.dumps(error_data, ensure_ascii=False, indent=2)}[/red]")

        self.message_completed = True

    async def send_message(self, text: str):
        """
        发送用户消息并等待响应完成。

        Args:
            text: 用户输入的文本
        """
        if not self.session_id:
            raise RuntimeError("会话未初始化")

        # 重置状态
        self.message_completed = False
        self.current_text_parts = {}
        self.current_tool_parts = {}

        # 显示用户消息
        self._print_panel(text, title="[bold blue]你[/bold blue]", border_style="blue")

        # 使用 ID 生成器生成消息ID和部分ID
        message_id = id_ascending('message')
        part_id = id_ascending('part')

        # 显示 AI 响应头
        self._print("\n[bold cyan]AI 助手:[/bold cyan] ", end='')

        # 创建消息部分
        parts = [
            message_create_params.PartTextPartInput(
                id=part_id,
                type='text',
                text=text,
                synthetic=False
            )
        ]

        # 发送消息
        try:
            await self.client.session.message.create(
                id=self.session_id,
                parts=parts,
                agent=self.agent_name or omit,
                message_id=message_id or omit,
                model=message_create_params.Model(
                    provider_id=self.provider_id,
                    model_id=self.model_id
                ) if self.provider_id and self.model_id else omit
            )
        except Exception as e:
            self._print(f"\n[bold red]发送消息失败:[/bold red] {e}")
            self.message_completed = True
            return

        # 等待响应完成
        while not self.message_completed:
            await asyncio.sleep(0.1)

        self._print()  # 最后的换行

    async def run(self):
        """运行交互式循环。"""
        self._print("\n[bold green]准备就绪![/bold green] 输入你的问题,输入 'exit', 'quit' 或 'q' 退出。\n")

        try:
            while True:
                # 获取用户输入 (在异步环境中使用同步input)
                try:
                    # 在异步环境中运行同步的input
                    loop = asyncio.get_event_loop()
                    if self.console:
                        user_input = await loop.run_in_executor(
                            None,
                            lambda: self.console.input("[bold]> [/bold]")
                        )
                        user_input = user_input.strip()
                    else:
                        user_input = await loop.run_in_executor(None, input, "> ")
                        user_input = user_input.strip()
                except (EOFError, KeyboardInterrupt):
                    break

                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'quit', 'q']:
                    break

                # 发送消息并显示响应
                try:
                    await self.send_message(user_input)
                except Exception as e:
                    self._print(f"\n[bold red]错误:[/bold red] {e}\n")

        finally:
            self._print("\n[yellow]正在关闭会话...[/yellow]")
            self.stop_event.set()
            if self.event_task:
                await asyncio.wait_for(self.event_task, timeout=2.0)
            self._print("[green]再见![/green]\n")

    async def close(self):
        """关闭客户端。"""
        self.stop_event.set()
        await self.client.close()


async def main():
    """主入口函数。"""
    import argparse

    parser = argparse.ArgumentParser(
        description='OpenCode 交互式终端 Agent (异步版本)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                                    # 连接到默认地址 localhost:3000
  %(prog)s --url http://localhost:8080       # 连接到自定义地址

环境变量:
  OPENCODE_SDK_BASE_URL                      # OpenCode 服务器地址
        """
    )
    parser.add_argument(
        '--url',
        default='http://localhost:3000',
        help='OpenCode 服务器地址 (默认: http://localhost:3000)'
    )

    args = parser.parse_args()

    # 创建并运行 agent
    agent = InteractiveTerminalAgent(base_url=args.url)

    try:
        await agent.initialize()
        await agent.run()
    except KeyboardInterrupt:
        print("\n\n用户中断。")
        sys.exit(0)
    except Exception as e:
        print(f"\n致命错误: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        await agent.close()


if __name__ == '__main__':
    asyncio.run(main())
