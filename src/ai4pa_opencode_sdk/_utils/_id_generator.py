import time
import secrets
import threading
from typing import Literal, Optional

# Type alias for prefix types
PrefixType = Literal['session', 'message', 'user', 'part', 'permission']


class IDGenerator:
    """
    Thread-safe ID generator compatible with OpenCode system.

    Generates IDs with the following format:
    - Prefix: 3 characters + underscore (e.g., 'ses_', 'msg_')
    - Timestamp: 12 hex characters (6 bytes, encodes millisecond timestamp + counter)
    - Random: 14 Base62 characters
    - Total length: 30 characters

    Features:
    - Monotonic: IDs are strictly increasing (or decreasing) within the same process
    - Thread-safe: Uses locks to ensure no duplicates in concurrent scenarios
    - Collision-resistant: Combines timestamp, counter, and random data
    - Sortable: IDs can be sorted chronologically
    """

    # Prefix constants
    PREFIXES = {
        'session': 'ses',
        'message': 'msg',
        'user': 'usr',
        'part': 'prt',
        'permission': 'per',
    }

    # ID component lengths
    LENGTH = 26  # Total length after prefix and underscore
    RANDOM_LENGTH = 14  # Length of random Base62 part

    # Base62 character set
    BASE62_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def __init__(self) -> None:
        """Initialize the ID generator with thread-safe state."""
        self._last_timestamp = 0
        self._counter = 0
        self._lock = threading.Lock()

    def ascending(self, prefix: PrefixType, given: Optional[str] = None) -> str:
        """
        Generate an ascending ID (newer IDs are greater).

        Args:
            prefix: Type of ID to generate ('session', 'message', 'user', 'part', 'permission')
            given: Optional existing ID to validate and return

        Returns:
            A unique ID string in format: {prefix}_{timestamp_hex}{random_base62}

        Raises:
            ValueError: If given ID doesn't start with the correct prefix

        Example:
            >>> gen = IDGenerator()
            >>> gen.id_ascending('session')
            'ses_18d4f5a3b2c1AbCd1234567890XyZw'
        """
        return self._generate_id(prefix, descending=False, given=given)

    def descending(self, prefix: PrefixType, given: Optional[str] = None) -> str:
        """
        Generate a descending ID (newer IDs are smaller).

        Uses bitwise NOT to reverse the timestamp, making newer IDs sort before older ones.

        Args:
            prefix: Type of ID to generate
            given: Optional existing ID to validate and return

        Returns:
            A unique ID string

        Example:
            >>> gen = IDGenerator()
            >>> gen.id_descending('message')
            'msg_e72b0a5c4d3eFgHi0987654321WvUt'
        """
        return self._generate_id(prefix, descending=True, given=given)

    def validate_prefix(self, id_string: str, prefix: PrefixType) -> bool:
        """
        Validate that an ID starts with the correct prefix.

        Args:
            id_string: The ID to validate
            prefix: Expected prefix type

        Returns:
            True if ID has the correct prefix, False otherwise

        Example:
            >>> gen = IDGenerator()
            >>> gen.validate_id_prefix('ses_123abc', 'session')
            True
            >>> gen.validate_id_prefix('msg_123abc', 'session')
            False
        """
        expected_prefix = self.PREFIXES[prefix]
        return id_string.startswith(expected_prefix + '_')

    def _generate_id(self, prefix: PrefixType, descending: bool, given: Optional[str] = None) -> str:
        """
        Internal method to generate or validate an ID.

        Args:
            prefix: Type of ID to generate
            descending: Whether to generate a descending ID
            given: Optional existing ID to validate

        Returns:
            Generated or validated ID string

        Raises:
            ValueError: If given ID has incorrect prefix
        """
        if given:
            expected_prefix = self.PREFIXES[prefix]
            if not given.startswith(expected_prefix + '_'):
                raise ValueError(f"ID '{given}' does not start with '{expected_prefix}_'")
            return given

        return self._create_new_id(prefix, descending)

    def _create_new_id(self, prefix: PrefixType, descending: bool) -> str:
        """
        Create a new unique ID.

        Thread-safe implementation that ensures monotonic ID generation.

        Args:
            prefix: Type of ID to generate
            descending: Whether to generate a descending ID

        Returns:
            Newly generated ID string
        """
        with self._lock:
            # Get current timestamp in milliseconds
            current_timestamp = int(time.time() * 1000)

            # Maintain monotonic counter
            if current_timestamp != self._last_timestamp:
                self._last_timestamp = current_timestamp
                self._counter = 0
            self._counter += 1

            # Combine timestamp and counter
            # Timestamp is left-shifted by 12 bits to make room for counter
            # This allows 4096 unique IDs per millisecond
            now = (current_timestamp * 0x1000) + self._counter

            # For descending IDs, bitwise NOT the value
            if descending:
                # In Python, we need to mask to 64 bits after NOT
                now = (~now) & 0xFFFFFFFFFFFFFFFF

            # Extract 6 bytes (48 bits) for timestamp portion
            time_bytes = bytearray(6)
            for i in range(6):
                time_bytes[i] = (now >> (40 - 8 * i)) & 0xFF

            # Generate random Base62 string
            random_part = self._random_base62(self.RANDOM_LENGTH)

            # Assemble the ID
            prefix_str = self.PREFIXES[prefix]
            time_hex = time_bytes.hex()

            return f"{prefix_str}_{time_hex}{random_part}"

    def _random_base62(self, length: int) -> str:
        """
        Generate a random Base62 string.

        Args:
            length: Number of characters to generate

        Returns:
            Random Base62 string
        """
        random_bytes = secrets.token_bytes(length)
        result = ''.join(
            self.BASE62_CHARS[byte % 62]
            for byte in random_bytes
        )
        return result


# Singleton instance for convenience
_default_generator = IDGenerator()


def id_ascending(prefix: PrefixType, given: Optional[str] = None) -> str:
    """
    Generate an ascending ID using the default generator.

    Convenience function for quick ID generation without instantiating IDGenerator.

    Args:
        prefix: Type of ID to generate
        given: Optional existing ID to validate

    Returns:
        Unique ascending ID

    Example:
        >>> session_id = id_ascending('session')
        >>> print(session_id)
    """
    return _default_generator.ascending(prefix, given)


def id_descending(prefix: PrefixType, given: Optional[str] = None) -> str:
    """
    Generate a descending ID using the default generator.

    Args:
        prefix: Type of ID to generate
        given: Optional existing ID to validate

    Returns:
        Unique descending ID

    Example:
        >>> msg_id = id_descending('message')
        >>> print(msg_id)
    """
    return _default_generator.descending(prefix, given)


def validate_id_prefix(id_string: str, prefix: PrefixType) -> bool:
    """
    Validate ID prefix using the default generator.

    Args:
        id_string: The ID to validate
        prefix: Expected prefix type

    Returns:
        True if valid, False otherwise

    Example:
        >>> validate_id_prefix('ses_123abc', 'session')
        True
    """
    return _default_generator.validate_prefix(id_string, prefix)
