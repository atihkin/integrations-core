# CHANGELOG - ECS Fargate

<!-- towncrier release notes start -->

## 4.1.0 / 2023-10-26

***Added***:

* Add storage_stats support for Windows ([#16014](https://github.com/DataDog/integrations-core/pull/16014))

***Fixed***:

* Fix blkio_stats bad metrics for Windows ([#16014](https://github.com/DataDog/integrations-core/pull/16014))

## 4.0.1 / 2023-08-25 / Agent 7.48.0

***Fixed***:

* Fix ECS Fargate memory task limit units ([#15656](https://github.com/DataDog/integrations-core/pull/15656))

## 4.0.0 / 2023-08-10

***Changed***:

* Bump the minimum base check version ([#15427](https://github.com/DataDog/integrations-core/pull/15427))

***Added***:

* Add task Memory Limit to ECS Fargate integration ([#15401](https://github.com/DataDog/integrations-core/pull/15401))
* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 3.4.0 / 2023-07-10 / Agent 7.47.0

***Added***:

* Add ephemeral storage metrics for fargate check ([#14775](https://github.com/DataDog/integrations-core/pull/14775))

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 3.3.0 / 2023-01-20 / Agent 7.43.0

***Added***:

* Add task CPU Limit to ECS Fargate integration and use nanocore as CPU unit ([#13551](https://github.com/DataDog/integrations-core/pull/13551))

## 3.2.0 / 2022-09-16 / Agent 7.40.0

***Added***:

* Update HTTP config spec templates ([#12890](https://github.com/DataDog/integrations-core/pull/12890))

## 3.1.1 / 2022-04-11 / Agent 7.36.0

***Fixed***:

* Remove outdated warning in the description for the `tls_ignore_warning` option ([#11800](https://github.com/DataDog/integrations-core/pull/11800))

## 3.1.0 / 2022-04-05

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

***Fixed***:

* Support newer versions of `click` ([#11746](https://github.com/DataDog/integrations-core/pull/11746))
* Remove outdated warning in the description for the `tls_ignore_warning` option ([#11591](https://github.com/DataDog/integrations-core/pull/11591))

## 3.0.0 / 2022-02-19 / Agent 7.35.0

***Changed***:

* Do not emit `ecs.fargate.mem.limit` metric when no memory hard-limit has been set ([#11484](https://github.com/DataDog/integrations-core/pull/11484))
* Add tls_protocols_allowed option documentation ([#11251](https://github.com/DataDog/integrations-core/pull/11251))

***Added***:

* Add `pyproject.toml` file ([#11342](https://github.com/DataDog/integrations-core/pull/11342))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 2.14.1 / 2022-01-08 / Agent 7.34.0

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 2.14.0 / 2021-11-13 / Agent 7.33.0

***Added***:

* Add Windows support for ECS Fargate ([#10521](https://github.com/DataDog/integrations-core/pull/10521))

***Fixed***:

* Fix CPU metrics on ECS Fargate ([#10409](https://github.com/DataDog/integrations-core/pull/10409))

## 2.13.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Add runtime configuration validation ([#8909](https://github.com/DataDog/integrations-core/pull/8909))
* Add HTTP option to control the size of streaming responses ([#10183](https://github.com/DataDog/integrations-core/pull/10183))
* Add allow_redirect option ([#10160](https://github.com/DataDog/integrations-core/pull/10160))

***Fixed***:

* Bump base package dependency ([#10218](https://github.com/DataDog/integrations-core/pull/10218))
* Fix the description of the `allow_redirects` HTTP option ([#10195](https://github.com/DataDog/integrations-core/pull/10195))

## 2.12.1 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 2.12.0 / 2021-01-25 / Agent 7.26.0

***Added***:

* Add new default for newly autodiscovered checks ([#8177](https://github.com/DataDog/integrations-core/pull/8177))

***Fixed***:

* Correct default template usage ([#8233](https://github.com/DataDog/integrations-core/pull/8233))

## 2.11.0 / 2020-12-11 / Agent 7.25.0

***Added***:

* Amazon fargate config specs ([#8003](https://github.com/DataDog/integrations-core/pull/8003))

## 2.10.0 / 2020-08-10 / Agent 7.22.0

***Added***:

* Support include/exclude containers in ECS Fargate ([#7165](https://github.com/DataDog/integrations-core/pull/7165))

***Fixed***:

* DOCS-838 Template wording ([#7038](https://github.com/DataDog/integrations-core/pull/7038))
* Update ntlm_domain example ([#7118](https://github.com/DataDog/integrations-core/pull/7118))

## 2.9.0 / 2020-06-29 / Agent 7.21.0

***Added***:

* Add note about warning concurrency ([#6967](https://github.com/DataDog/integrations-core/pull/6967))

## 2.8.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))

## 2.7.0 / 2020-04-04 / Agent 7.19.0

***Added***:

* Collect network metrics for ECS Fargate ([#6216](https://github.com/DataDog/integrations-core/pull/6216))

***Fixed***:

* Update deprecated imports ([#6088](https://github.com/DataDog/integrations-core/pull/6088))

## 2.6.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Use lazy logging format ([#5377](https://github.com/DataDog/integrations-core/pull/5377))

***Fixed***:

* Fix CPU metrics ([#5404](https://github.com/DataDog/integrations-core/pull/5404))

## 2.5.0 / 2019-12-02 / Agent 7.16.0

***Added***:

* Add auth type to RequestsWrapper ([#4708](https://github.com/DataDog/integrations-core/pull/4708))

## 2.4.0 / 2019-10-11 / Agent 6.15.0

***Added***:

* Add option to override KRB5CCNAME env var ([#4578](https://github.com/DataDog/integrations-core/pull/4578))

***Fixed***:

* Fix ecs_fargate timeout ([#4518](https://github.com/DataDog/integrations-core/pull/4518))

## 2.3.0 / 2019-08-24 / Agent 6.14.0

***Added***:

* Update with proxy settings and request wrapper ([#3477](https://github.com/DataDog/integrations-core/pull/3477))

## 2.2.2 / 2019-07-17 / Agent 6.13.0

***Fixed***:

* Use tagger with container_id prefix ([#4126](https://github.com/DataDog/integrations-core/pull/4126))

## 2.2.1 / 2019-06-28 / Agent 6.12.1

***Fixed***:

* Make the kubelet and ECS fargate checks resilient to the tagger returning None ([#4004](https://github.com/DataDog/integrations-core/pull/4004))

## 2.2.0 / 2019-05-14 / Agent 6.12.0

***Added***:

* Adhere to code style ([#3503](https://github.com/DataDog/integrations-core/pull/3503))

## 2.1.0 / 2019-02-18 / Agent 6.10.0

***Added***:

* Support Python 3 ([#2885](https://github.com/DataDog/integrations-core/pull/2885))

## 2.0.0 / 2018-11-30 / Agent 6.8.0

***Changed***:

* Rework tagging to be consistent with the live container view and Autodiscovery ([#2601][1])

## 1.3.0 / 2018-09-11 / Agent 6.5.0

***Added***:

* Add cpu percent metric and fix container stopped behaviour ([#2206][2])

## 1.2.1 / 2018-09-04

***Fixed***:

* Fix key errors ([#1959][3])
* Update metadata of the cpu metrics from gauges to rates ([#1518][4])
* Add data files to the wheel package ([#1727][5])

## 1.2.0 / 2018-05-11

***Added***:

* add an integration tile in the app for Fargate.

***Fixed***:

* update the metadata collected from Version to Revision.

## 1.1.0/ 2018-03-23

***Added***:

* adds custom tag support to service checks.
* make the fargate conf file docker friendly.

## 1.0.0/ 2018-02-28

***Added***:

* adds ecs_fargate integration.

[1]: https://github.com/DataDog/integrations-core/pull/2601
[2]: https://github.com/DataDog/integrations-core/pull/2206
[3]: https://github.com/DataDog/integrations-core/pull/1959
[4]: https://github.com/DataDog/integrations-core/pull/1518
[5]: https://github.com/DataDog/integrations-core/pull/1727