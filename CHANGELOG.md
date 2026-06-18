# Changelog

## 0.2.0 (2026-06-18)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/stainless-commons/stripe-python/compare/v0.1.0...v0.2.0)

### Features

* **internal:** implement indices array format for query and form serialization ([17ab3f3](https://github.com/stainless-commons/stripe-python/commit/17ab3f3c1d2dadb6f357a9e61df025bd4ee0129a))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([fb89f44](https://github.com/stainless-commons/stripe-python/commit/fb89f44fe38a01b3fd386ea71c2db9b26a5963dc))
* **deps:** bump minimum typing-extensions version ([a345ecd](https://github.com/stainless-commons/stripe-python/commit/a345ecd2ac41ef6d61458b205ed98319a524f0c8))
* ensure file data are only sent as 1 parameter ([9099ed6](https://github.com/stainless-commons/stripe-python/commit/9099ed6e7425449bf0e0579f53b6ea141787d3f2))
* **pydantic:** do not pass `by_alias` unless set ([0449b45](https://github.com/stainless-commons/stripe-python/commit/0449b453ecc7f71d93c2e027a20d452ad3ab7c87))
* sanitize endpoint path params ([35bfff2](https://github.com/stainless-commons/stripe-python/commit/35bfff2629faeada215bcd5ec87892295d9ee500))
* use correct format for nested and array query params ([aed61b7](https://github.com/stainless-commons/stripe-python/commit/aed61b71afd19864976d3202e6d2b48cadae2ee8))


### Chores

* bump @stdy/cli to 0.15.3 ([3847ce1](https://github.com/stainless-commons/stripe-python/commit/3847ce1c5966a6ec456b3c831c7b275f37c17b34))
* **ci:** bump uv version ([e3f69aa](https://github.com/stainless-commons/stripe-python/commit/e3f69aac9b1c86932148e536fff17919224e4b3d))
* **ci:** skip lint on metadata-only changes ([d93c7cf](https://github.com/stainless-commons/stripe-python/commit/d93c7cffbc6b2219bd7daefe997c900fea976fdc))
* **ci:** skip uploading artifacts on stainless-internal branches ([3cd3725](https://github.com/stainless-commons/stripe-python/commit/3cd37254e2c8d4f81525c91263b6d76ce234250a))
* format all `api.md` files ([c48c11d](https://github.com/stainless-commons/stripe-python/commit/c48c11d7ded34e0caebe970203291c68ba9552fb))
* **internal:** add request options to SSE classes ([fa41519](https://github.com/stainless-commons/stripe-python/commit/fa41519a4d2313962ac322d782d1f70265b6d0ba))
* **internal:** bump mock server version ([44e6bfb](https://github.com/stainless-commons/stripe-python/commit/44e6bfb11bb60d74b96418f93dad036d5e286d71))
* **internal:** codegen related update ([34853f3](https://github.com/stainless-commons/stripe-python/commit/34853f315bafea90fcc8eac3e675d41db64a75b6))
* **internal:** codegen related update ([7281455](https://github.com/stainless-commons/stripe-python/commit/7281455bf015da226d3dc5ecd9373924d779716a))
* **internal:** codegen related update ([25caceb](https://github.com/stainless-commons/stripe-python/commit/25caceb60320734674a5a333109d427eb0b9fec9))
* **internal:** codegen related update ([a665c40](https://github.com/stainless-commons/stripe-python/commit/a665c40437d9b383bd5c015f675153c5b876517e))
* **internal:** codegen related update ([7d3763e](https://github.com/stainless-commons/stripe-python/commit/7d3763eadb0a7fb5e58371592ebade2472ba8c3a))
* **internal:** codegen related update ([32491ca](https://github.com/stainless-commons/stripe-python/commit/32491ca9d2543d11b3dc90c0904cab9ab77cc462))
* **internal:** codegen related update ([65ba06e](https://github.com/stainless-commons/stripe-python/commit/65ba06e655539c6bf8d41449fc8516417848ba97))
* **internal:** codegen related update ([17b695e](https://github.com/stainless-commons/stripe-python/commit/17b695ecd0532acd0e19af3ee266ce3514a34a82))
* **internal:** codegen related update ([80e4496](https://github.com/stainless-commons/stripe-python/commit/80e449622d08e15eaba286c60f12955ff49cb051))
* **internal:** make `test_proxy_environment_variables` more resilient ([09dfc73](https://github.com/stainless-commons/stripe-python/commit/09dfc739821286e53d3faef95946384e7de6ed7a))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([ee9ae9e](https://github.com/stainless-commons/stripe-python/commit/ee9ae9efd7b7596ed7e9ff7345058fc55df2b9f0))
* **internal:** refactor authentication internals ([50a4731](https://github.com/stainless-commons/stripe-python/commit/50a4731ff1da1cf30e789e081d3c0d7cafd977a1))
* **internal:** tweak CI branches ([0aafb30](https://github.com/stainless-commons/stripe-python/commit/0aafb30d64e513a37c14551533fabf353026ed13))
* **internal:** update gitignore ([468b5ec](https://github.com/stainless-commons/stripe-python/commit/468b5ec187aea033e4b993334e6a58d4004ea2c9))
* **test:** do not count install time for mock server timeout ([73fc33b](https://github.com/stainless-commons/stripe-python/commit/73fc33bf6ba7759a4bf5b8ce672f4866d744f628))
* **test:** enable generated tests ([81c8402](https://github.com/stainless-commons/stripe-python/commit/81c84023ed762036e97a88e85684cc5fa25d1adf))
* **tests:** bump @stdy/cli to 0.16.1 ([1b8ece0](https://github.com/stainless-commons/stripe-python/commit/1b8ece00e53ee181f69119e1925c24afc2319428))
* **tests:** bump mock server version ([e306ac0](https://github.com/stainless-commons/stripe-python/commit/e306ac08b2eb0d0385aa5d26c6b540a1988382eb))
* **tests:** bump steady to v0.19.4 ([5411b66](https://github.com/stainless-commons/stripe-python/commit/5411b66e3ecf143da5fd0d2280bb35a07b192585))
* **tests:** bump steady to v0.19.5 ([f2d5d32](https://github.com/stainless-commons/stripe-python/commit/f2d5d329055049db5a46643a3d531e210b69028a))
* **tests:** bump steady to v0.19.6 ([fee581f](https://github.com/stainless-commons/stripe-python/commit/fee581fddb74d78b5dc980cd98037291b1a1368b))
* **tests:** bump steady to v0.19.7 ([24b91ef](https://github.com/stainless-commons/stripe-python/commit/24b91efc0b1d6fc51c673701a09a8e80dfb57590))
* **tests:** bump steady to v0.20.1 ([2cdebcb](https://github.com/stainless-commons/stripe-python/commit/2cdebcb70d3b9e880766370c8f140bf5b615a4b4))
* **tests:** bump steady to v0.20.2 ([c62b77b](https://github.com/stainless-commons/stripe-python/commit/c62b77b128486421f209a4d36cd376a363224960))
* update mock server docs ([bcd2711](https://github.com/stainless-commons/stripe-python/commit/bcd27117fb081aa59df24e034678c8dea078259b))


### Documentation

* improve examples ([eed185a](https://github.com/stainless-commons/stripe-python/commit/eed185a397e3447a11bdbb420aeacd04f7852b46))

## 0.1.0 (2026-02-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/stainless-commons/stripe-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([ddd39ed](https://github.com/stainless-commons/stripe-python/commit/ddd39ede1ff627a4a42ccfc6bdcc29382ecd4062))
* **api:** manual updates ([ce1515f](https://github.com/stainless-commons/stripe-python/commit/ce1515f3fb170f94aa753e2666413aecc34f67da))
* **api:** manual updates ([a22587f](https://github.com/stainless-commons/stripe-python/commit/a22587fc6d881abd3bcc53efe762d19f25aef885))
* **api:** manual updates ([d0f9b47](https://github.com/stainless-commons/stripe-python/commit/d0f9b47163845d40481b333e007fd5ae1c2d1243))
* **api:** manual updates ([df4c50a](https://github.com/stainless-commons/stripe-python/commit/df4c50a4dbefd67c64bedf4274fc532817846b6b))
* **api:** manual updates ([b7b117d](https://github.com/stainless-commons/stripe-python/commit/b7b117d9e76b72b742a84949941e1c3b65515c39))
* **api:** manual updates ([c1b8542](https://github.com/stainless-commons/stripe-python/commit/c1b8542c564d7d99c517db2d76377b0027ac7521))
* **api:** manual updates ([c7f7de4](https://github.com/stainless-commons/stripe-python/commit/c7f7de4693baad277cf7b24302726f03be52d69b))
* **api:** manual updates ([cb59e1e](https://github.com/stainless-commons/stripe-python/commit/cb59e1e0637785af584fb3bc5b1000425d01c310))


### Chores

* configure new SDK language ([02968ed](https://github.com/stainless-commons/stripe-python/commit/02968ed41bf10f2a743e72a2b5392b51e7029b26))
* **internal:** bump dependencies ([5daccfb](https://github.com/stainless-commons/stripe-python/commit/5daccfb96d5dd463a565fd4b33156d2f97209b09))
* **internal:** fix lint error on Python 3.14 ([1e62e09](https://github.com/stainless-commons/stripe-python/commit/1e62e099378219f3d5861a5d58a82656e69af17b))
* update SDK settings ([f0c66c1](https://github.com/stainless-commons/stripe-python/commit/f0c66c117f33fdf6b95643fead0d6e798c6d2ec0))
