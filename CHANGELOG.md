# Changelog

## 0.18.0 (2026-07-18)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/kaaass/opencode-sdk/compare/v0.17.0...v0.18.0)

### Features

* **stlc:** configurable CI runner and private-production-repo support in workflow templates ([b0bf3e2](https://github.com/kaaass/opencode-sdk/commit/b0bf3e284f397e82841b011bb505170a3ab7f613))


### Bug Fixes

* **auth:** prioritize first auth header ([59f11ac](https://github.com/kaaass/opencode-sdk/commit/59f11ac101c724275492316987dfd7e04c94756e))
* **internal:** resolve build failures ([ceed60c](https://github.com/kaaass/opencode-sdk/commit/ceed60ce4bdc6351d5201e856e5c1b4f16d1dd35))
* **types:** avoid type-checker errors on params with additional properties ([34c9e59](https://github.com/kaaass/opencode-sdk/commit/34c9e59361e127d550ecc07e1c915ba8a6176c0d))

## 0.17.0 (2026-06-05)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/kaaass/opencode-sdk/compare/v0.16.0...v0.17.0)

### Features

* **api:** 1.2.0 ([390239b](https://github.com/kaaass/opencode-sdk/commit/390239bede5d0705eba6cbd9e51690e56f177e4d))
* **internal/types:** support eagerly validating pydantic iterators ([f1202b6](https://github.com/kaaass/opencode-sdk/commit/f1202b6c824fd35d7775b237e130f9b796ae1629))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([3c3faa9](https://github.com/kaaass/opencode-sdk/commit/3c3faa98e47523815bc04d2763f800efb6cae789))

## 0.16.0 (2026-05-06)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/kaaass/opencode-sdk/compare/v0.15.0...v0.16.0)

### Features

* **api:** 1.1.0 ([8217193](https://github.com/kaaass/opencode-sdk/commit/82171935d1f2d3d1f10b03fa0304423a356b1946))
* support setting headers via env ([3edf431](https://github.com/kaaass/opencode-sdk/commit/3edf4318c1c68cd91a15e264fd020d6854671fe2))


### Bug Fixes

* use correct field name format for multipart file arrays ([bcf3b16](https://github.com/kaaass/opencode-sdk/commit/bcf3b167a12d4ced14b91b2f1e347e7bfe1a2291))


### Chores

* **internal:** reformat pyproject.toml ([67b1b99](https://github.com/kaaass/opencode-sdk/commit/67b1b99bb43102c0b6fdaee9bae2871dd1bab512))

## 0.15.0 (2026-04-25)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/kaaass/opencode-sdk/compare/v0.14.0...v0.15.0)

### Features

* **api:** bump to api 1.0.0 ([5045406](https://github.com/kaaass/opencode-sdk/commit/50454067cb05ec128e94e631f7cb3fd16c32daec))
* **api:** manual updates ([ccade69](https://github.com/kaaass/opencode-sdk/commit/ccade69509a4098f39d4c67af0cbb38752da96b8))
* **api:** manual updates ([7dd823b](https://github.com/kaaass/opencode-sdk/commit/7dd823b9eb5ab37c5c6e433ab3e1e443259f7ae9))
* **api:** manual updates ([477d11a](https://github.com/kaaass/opencode-sdk/commit/477d11a46e108ed8ecefed6383aee8a45ed3578b))
* **internal:** implement indices array format for query and form serialization ([bfdec21](https://github.com/kaaass/opencode-sdk/commit/bfdec2118979c5b885a13caf8565b2e708fa6ca3))


### Bug Fixes

* break circular import between shared.agent_config and global_.config ([6493d6a](https://github.com/kaaass/opencode-sdk/commit/6493d6ae8247f66574b464bd504a2b277d976828))
* **client:** preserve hardcoded query params when merging with user params ([dd9e1f1](https://github.com/kaaass/opencode-sdk/commit/dd9e1f17355b2f41c8af665845f4e8209d490a81))
* **deps:** bump minimum typing-extensions version ([f042cd3](https://github.com/kaaass/opencode-sdk/commit/f042cd35830012f90fa02ceeb6685d5d604b2151))
* ensure file data are only sent as 1 parameter ([50393e7](https://github.com/kaaass/opencode-sdk/commit/50393e7ef3c03056ff6b8156632ec34be85aaa6c))
* **examples:** migrate imports to renamed ai4pa_opencode_sdk package ([10c797c](https://github.com/kaaass/opencode-sdk/commit/10c797c5ea10fe4ee8225bad605170a7daeec0f9))
* **pydantic:** do not pass `by_alias` unless set ([247d93c](https://github.com/kaaass/opencode-sdk/commit/247d93c89876ff34864fef1b75579396fa85ebba))
* resolve lint errors blocking import and type checks ([712795e](https://github.com/kaaass/opencode-sdk/commit/712795eca71c739fd44a2ce9199e5393e4dd827a))
* sanitize endpoint path params ([085a631](https://github.com/kaaass/opencode-sdk/commit/085a6316713e19ab7c809e9ce59e94264faa694b))


### Chores

* **ci:** skip lint on metadata-only changes ([62c3321](https://github.com/kaaass/opencode-sdk/commit/62c33213773362644326abd6f5f5ea2a006fad4c))
* **ci:** skip uploading artifacts on stainless-internal branches ([c7bd25c](https://github.com/kaaass/opencode-sdk/commit/c7bd25c1090378c3a153e2f8c438a92bf46e7aa8))
* **internal:** add request options to SSE classes ([f2112ca](https://github.com/kaaass/opencode-sdk/commit/f2112cae8151f290c8b9713bcd88850216fe47c9))
* **internal:** make `test_proxy_environment_variables` more resilient ([f2ab602](https://github.com/kaaass/opencode-sdk/commit/f2ab60212008d2217eb1251ac04d903d216f6dd6))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([6afec94](https://github.com/kaaass/opencode-sdk/commit/6afec948814d0515e8ec4d409246001c5a62c63e))
* **internal:** remove mock server code ([2292d6a](https://github.com/kaaass/opencode-sdk/commit/2292d6a0ee39b5269ace95e035fa5e717484cf98))
* **internal:** tweak CI branches ([3fd5481](https://github.com/kaaass/opencode-sdk/commit/3fd5481f72f4bb6eae956e7a3c639d8d9bf2fd24))
* **internal:** update gitignore ([f763b1b](https://github.com/kaaass/opencode-sdk/commit/f763b1ba38caf7ac05e479a448277dadc6440af2))
* **test:** update skip reason message ([1fc3871](https://github.com/kaaass/opencode-sdk/commit/1fc38715a9bedf39f8c90b44cf7103133a961d65))
* update mock server docs ([c6b9085](https://github.com/kaaass/opencode-sdk/commit/c6b9085245980e8679b2ef301be895d33c00fc12))
* update placeholder string ([7663692](https://github.com/kaaass/opencode-sdk/commit/766369290eca47050773790b81046fbab4aa1ce9))
* update SDK settings ([77a3f6e](https://github.com/kaaass/opencode-sdk/commit/77a3f6e8a3a31ef6806d5311f9683d1db29ee321))


### Documentation

* improve examples ([45428ca](https://github.com/kaaass/opencode-sdk/commit/45428ca07f73c5666e9958e035d5c52bff4bb7bc))


### Refactors

* **types:** use `extra_items` from PEP 728 ([65eb397](https://github.com/kaaass/opencode-sdk/commit/65eb3974b33b12d192eadebaa6f0c7e6b97828bd))

## 0.14.0 (2026-02-13)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/kaaass/opencode-sdk/compare/v0.13.0...v0.14.0)

### Features

* **api:** 0.12.1 ([2951395](https://github.com/kaaass/opencode-sdk/commit/2951395836127c8e1c7ca8b1681b664965d02a4c))


### Chores

* format all `api.md` files ([3fc3f72](https://github.com/kaaass/opencode-sdk/commit/3fc3f72b96c40f548d9e0c0ea223ae3b745ebeec))
* **internal:** fix lint error on Python 3.14 ([a534952](https://github.com/kaaass/opencode-sdk/commit/a534952d38ca42d7ea1204e905d58503fdb63ccd))

## 0.13.0 (2026-02-11)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/kaaass/opencode-sdk/compare/v0.12.0...v0.13.0)

### Features

* **api:** manual updates ([ee11e4c](https://github.com/kaaass/opencode-sdk/commit/ee11e4cbb6d3b3b7a0a43d0a89155742ed4bded8))

## 0.12.0 (2026-02-10)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/kaaass/opencode-sdk/compare/v0.11.0...v0.12.0)

### Features

* **api:** client skill ([29d65bb](https://github.com/kaaass/opencode-sdk/commit/29d65bbdff4998ec73740e67ca97222402f6bb1a))
* **client:** add custom JSON encoder for extended type support ([5be0a19](https://github.com/kaaass/opencode-sdk/commit/5be0a19d885978f53d1cc55733d0a984e727457a))


### Bug Fixes

* **types:** correctly define false enum ([2994304](https://github.com/kaaass/opencode-sdk/commit/2994304d234353a58f0c714c6738bd99eb7b7907))


### Chores

* **ci:** upgrade `actions/github-script` ([a0564a0](https://github.com/kaaass/opencode-sdk/commit/a0564a02048db4bd7468eaf7b7fa6b02976ca7a6))
* **internal:** bump dependencies ([b6448b2](https://github.com/kaaass/opencode-sdk/commit/b6448b2e4b4e652809fae7a8a6d43f424bfa2b00))

## 0.11.0 (2026-01-19)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/kaaass/opencode-sdk/compare/v0.10.0...v0.11.0)

### Features

* **api:** 0.11.0 ([8ec6cc9](https://github.com/kaaass/opencode-sdk/commit/8ec6cc9a991d2f25e05104cf2183fc346acc7c8b))


### Chores

* **internal:** update `actions/checkout` version ([c35a4e7](https://github.com/kaaass/opencode-sdk/commit/c35a4e7d036258fc51cabd00359736a3af56718b))

## 0.10.0 (2026-01-15)

Full Changelog: [v0.9.2...v0.10.0](https://github.com/kaaass/opencode-sdk/compare/v0.9.2...v0.10.0)

### Features

* **api:** manual updates ([793be18](https://github.com/kaaass/opencode-sdk/commit/793be1814fdd1b0f336c4ba6b30be9bfca614928))

## 0.9.2 (2026-01-14)

Full Changelog: [v0.9.1...v0.9.2](https://github.com/kaaass/opencode-sdk/compare/v0.9.1...v0.9.2)

## 0.9.1 (2026-01-14)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/kaaass/opencode-sdk/compare/v0.9.0...v0.9.1)

### Chores

* update SDK settings ([f4f9fe3](https://github.com/kaaass/opencode-sdk/commit/f4f9fe3087d118b5a7b0188a319d95e1be0249e5))

## 0.9.0 (2026-01-14)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/kaaass/opencode-sdk/compare/v0.8.0...v0.9.0)

### Features

* **client:** add support for binary request streaming ([5bde958](https://github.com/kaaass/opencode-sdk/commit/5bde958cfb80d482c2d9a0524c2ddf38b72bf6c1))


### Build System

* **ci:** 增加发布到 github 的 workflow ([96b8e7e](https://github.com/kaaass/opencode-sdk/commit/96b8e7ebb1bcf131d19276704d19751c206cbbca))

## 0.8.0 (2026-01-13)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/kaaass/opencode-sdk/compare/v0.7.0...v0.8.0)

### ⚠ BREAKING CHANGES

* **api:** remote tool -> client tool

### Bug Fixes

* **client:** loosen auth header validation ([8dea4e8](https://github.com/kaaass/opencode-sdk/commit/8dea4e82ea8a331e9518c4168d7c8a91801b175c))


### Chores

* **internal:** codegen related update ([c59ddd9](https://github.com/kaaass/opencode-sdk/commit/c59ddd9c8bf8a40bd5afb948ec2aad889d3f2111))


### Refactors

* **api:** remote tool -&gt; client tool ([1941c04](https://github.com/kaaass/opencode-sdk/commit/1941c04212d04dca556b5335ba24690072b45917))

## 0.7.0 (2025-12-23)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/kaaass/opencode-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** manual updates ([3bfb82f](https://github.com/kaaass/opencode-sdk/commit/3bfb82f6d929c269f1efe6af2b54f599c61ae8f2))


### Documentation

* add more examples ([be089c6](https://github.com/kaaass/opencode-sdk/commit/be089c6e77900e2ee9e54aa8efc174757039ec47))

## 0.6.0 (2025-12-19)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/kaaass/opencode-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([e1fe3e4](https://github.com/kaaass/opencode-sdk/commit/e1fe3e4bff84415819fe1fac815db24d3f48b32b))


### Bug Fixes

* use async_to_httpx_files in patch method ([c664f2a](https://github.com/kaaass/opencode-sdk/commit/c664f2a0202a5ffffd97345a007b37b00c3bb5e1))


### Chores

* **internal:** add `--fix` argument to lint script ([6c142b9](https://github.com/kaaass/opencode-sdk/commit/6c142b9db772d6ecd4a9d30a61a79ee3ffa9651c))

## 0.5.0 (2025-12-18)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/kaaass/opencode-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** manual updates ([da1be86](https://github.com/kaaass/opencode-sdk/commit/da1be86427ef798f03a59cb1e40d8a52eaf6f929))


### Chores

* speedup initial import ([0dc9494](https://github.com/kaaass/opencode-sdk/commit/0dc94940e7297a62826e3f38fd904d1a02862fff))

## 0.4.0 (2025-12-16)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/kaaass/opencode-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** manual updates ([46a3e21](https://github.com/kaaass/opencode-sdk/commit/46a3e2192d9da14896903cd76866c26508d36bfb))
* **api:** manual updates ([44d6718](https://github.com/kaaass/opencode-sdk/commit/44d67180099235b10c77a23ad0ab48f9b110e594))
* support ignore verify ssl ([e0f68b1](https://github.com/kaaass/opencode-sdk/commit/e0f68b105a5c4d3969a6a7decf61ead7c7f214ea))


### Bug Fixes

* **client:** close streams without requiring full consumption ([5d28f21](https://github.com/kaaass/opencode-sdk/commit/5d28f212e6e160a8dd4e63546504a32a7425bc13))
* compat with Python 3.14 ([9809dba](https://github.com/kaaass/opencode-sdk/commit/9809dba8de93349cc817d1a620913ad0a7e38f31))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([5e3454a](https://github.com/kaaass/opencode-sdk/commit/5e3454a2558e4b50a1c4aa501f131d6ba346bba1))
* ensure streams are always closed ([94be881](https://github.com/kaaass/opencode-sdk/commit/94be881651e6429627a51c77e385f06c46ce5de5))
* lint issue ([844a772](https://github.com/kaaass/opencode-sdk/commit/844a772b2605df7892704b756bbf39b259e0d52c))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([0cefe34](https://github.com/kaaass/opencode-sdk/commit/0cefe343e91bf60b1a677755eb10228c329e3d18))
* unit test failed ([79f6d34](https://github.com/kaaass/opencode-sdk/commit/79f6d34cedce3154d65b5fff04b40338f873f927))


### Chores

* add missing docstrings ([a3e6cb8](https://github.com/kaaass/opencode-sdk/commit/a3e6cb8dbd206da21495b0cb3863b7cee44f74b6))
* add Python 3.14 classifier and testing ([9acb5bd](https://github.com/kaaass/opencode-sdk/commit/9acb5bd24753cc935af0688b97e8a3e5229f4a9e))
* bump `httpx-aiohttp` version to 0.1.9 ([a1a5f99](https://github.com/kaaass/opencode-sdk/commit/a1a5f99195f371340242a5cadb1ef865b905960d))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([63eef0e](https://github.com/kaaass/opencode-sdk/commit/63eef0e91cae2b7566f336fd7587224359a7ba97))
* **docs:** use environment variables for authentication in code snippets ([8955cd2](https://github.com/kaaass/opencode-sdk/commit/8955cd264139ce8d3d0f251e73ad2988fe663654))
* **internal/tests:** avoid race condition with implicit client cleanup ([b37fc61](https://github.com/kaaass/opencode-sdk/commit/b37fc6125dbff5992b3f3d67b3e9d3124b8f10a5))
* **internal:** add missing files argument to base client ([cdfbe1d](https://github.com/kaaass/opencode-sdk/commit/cdfbe1d956fae14d6ac9485ef794dc291fadbcd3))
* **internal:** grammar fix (it's -&gt; its) ([d4eac90](https://github.com/kaaass/opencode-sdk/commit/d4eac9006c19f7c7ed5e3b4a03fccbc069a36b95))
* **package:** drop Python 3.8 support ([209976f](https://github.com/kaaass/opencode-sdk/commit/209976f6d21161803d2e31b66417d3a446d3865a))
* update lockfile ([8d6b327](https://github.com/kaaass/opencode-sdk/commit/8d6b32704b61ac9da3e62551f1823aedbfb4d36d))

## 0.3.0 (2025-10-17)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/kaaass/opencode-sdk/compare/v0.2.0...v0.3.0)

### Features

* **api:** manual updates ([372d719](https://github.com/kaaass/opencode-sdk/commit/372d719511d90b2a942fcd8b7f8eb091dbec2538))

## 0.2.0 (2025-10-15)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/kaaass/opencode-sdk/compare/v0.1.0...v0.2.0)

### Features

* **api:** manual updates ([3d2a739](https://github.com/kaaass/opencode-sdk/commit/3d2a739f17e9251ab088b57334d46c2fa75054e4))
* **example:** add interactive agent example ([df2f077](https://github.com/kaaass/opencode-sdk/commit/df2f0778dde311bcc050f0edb25c10150b9e34f4))
* implement id generator ([1ec62e8](https://github.com/kaaass/opencode-sdk/commit/1ec62e8808fd9b7d8c759c9fddf96fd27551ba91))

## 0.1.0 (2025-10-15)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/kaaass/opencode-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([8a02796](https://github.com/kaaass/opencode-sdk/commit/8a02796dcea8eeb6bcbbc4b6ffba98507f7f8b45))


### Chores

* update SDK settings ([0fe2954](https://github.com/kaaass/opencode-sdk/commit/0fe29544786d4daa5c412e531a42e8a34fc10311))
