# CHANGELOG - mesos_slave

<!-- towncrier release notes start -->

## 3.2.1 / 2023-08-18 / Agent 7.48.0

***Fixed***:

* Update datadog-checks-base dependency version to 32.6.0 ([#15604](https://github.com/DataDog/integrations-core/pull/15604))

## 3.2.0 / 2023-08-10

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 3.1.1 / 2023-07-10 / Agent 7.47.0

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 3.1.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

***Fixed***:

* Remove outdated warning in the description for the `tls_ignore_warning` option ([#11591](https://github.com/DataDog/integrations-core/pull/11591))

## 3.0.0 / 2022-02-19 / Agent 7.35.0

***Changed***:

* Add tls_protocols_allowed option documentation ([#11251](https://github.com/DataDog/integrations-core/pull/11251))

***Added***:

* Add `pyproject.toml` file ([#11398](https://github.com/DataDog/integrations-core/pull/11398))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 2.11.1 / 2022-01-08 / Agent 7.34.0

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 2.11.0 / 2021-10-04 / Agent 7.32.0

***Added***:

* Add HTTP option to control the size of streaming responses ([#10183](https://github.com/DataDog/integrations-core/pull/10183))
* Add allow_redirect option ([#10160](https://github.com/DataDog/integrations-core/pull/10160))
* Disable generic tags ([#10027](https://github.com/DataDog/integrations-core/pull/10027))

***Fixed***:

* Fix the description of the `allow_redirects` HTTP option ([#10195](https://github.com/DataDog/integrations-core/pull/10195))

## 2.10.1 / 2021-07-15 / Agent 7.30.0

***Fixed***:

* Improve cluster_name config option description ([#9704](https://github.com/DataDog/integrations-core/pull/9704))

## 2.10.0 / 2021-07-12

***Added***:

* Add runtime configuration validation ([#8956](https://github.com/DataDog/integrations-core/pull/8956))

## 2.9.0 / 2021-06-09

***Added***:

* Add `cluster_name` config option ([#9477](https://github.com/DataDog/integrations-core/pull/9477)) Thanks [dfreilich](https://github.com/dfreilich).

## 2.8.0 / 2021-04-19 / Agent 7.28.0

***Added***:

* Add log support ([#8717](https://github.com/DataDog/integrations-core/pull/8717))

## 2.7.1 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 2.7.0 / 2020-11-06 / Agent 7.24.0

***Added***:

* Update HTTP config docs to describe dcos_auth token reader ([#7953](https://github.com/DataDog/integrations-core/pull/7953))

## 2.6.0 / 2020-10-31

***Added***:

* Add ability to dynamically get authentication information ([#7660](https://github.com/DataDog/integrations-core/pull/7660))

## 2.5.0 / 2020-09-21 / Agent 7.23.0

***Added***:

* Add RequestsWrapper option to support UTF-8 for basic auth ([#7441](https://github.com/DataDog/integrations-core/pull/7441))

***Fixed***:

* Update proxy section in conf.yaml ([#7336](https://github.com/DataDog/integrations-core/pull/7336))

## 2.4.0 / 2020-08-10 / Agent 7.22.0

***Added***:

* Add config specs ([#7292](https://github.com/DataDog/integrations-core/pull/7292))

***Fixed***:

* Update ntlm_domain example ([#7118](https://github.com/DataDog/integrations-core/pull/7118))

## 2.3.0 / 2020-06-29 / Agent 7.21.0

***Added***:

* Add note about warning concurrency ([#6967](https://github.com/DataDog/integrations-core/pull/6967))

## 2.2.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))

## 2.1.1 / 2020-04-04 / Agent 7.19.0

***Fixed***:

* Update deprecated imports ([#6088](https://github.com/DataDog/integrations-core/pull/6088))

## 2.1.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Use lazy logging format ([#5377](https://github.com/DataDog/integrations-core/pull/5377))

## 2.0.1 / 2019-12-04 / Agent 7.16.0

***Fixed***:

* Propagate tags properly to stats metrics ([#5140](https://github.com/DataDog/integrations-core/pull/5140))

## 2.0.0 / 2019-12-02

***Changed***:

* Refactor code and properly send a service check for each endpoint ([#4891](https://github.com/DataDog/integrations-core/pull/4891))

***Fixed***:

* Fix service check message ([#4771](https://github.com/DataDog/integrations-core/pull/4771))

## 1.6.0 / 2019-10-11 / Agent 6.15.0

***Added***:

* Add option to override KRB5CCNAME env var ([#4578](https://github.com/DataDog/integrations-core/pull/4578))

## 1.5.1 / 2019-08-28 / Agent 6.14.0

***Fixed***:

* Fix mesos_slave service check ([#4448](https://github.com/DataDog/integrations-core/pull/4448))

## 1.5.0 / 2019-08-24

***Added***:

* Add requests wrapper to mesos_slave ([#4222](https://github.com/DataDog/integrations-core/pull/4222))
* Add support for /state endpoint ([#4054](https://github.com/DataDog/integrations-core/pull/4054))

## 1.4.1 / 2019-06-01 / Agent 6.12.0

***Fixed***:

* Fix code style ([#3838](https://github.com/DataDog/integrations-core/pull/3838))

## 1.4.0 / 2019-05-14

***Added***:

* Adhere to code style ([#3539](https://github.com/DataDog/integrations-core/pull/3539))

## 1.3.0 / 2019-02-18 / Agent 6.10.0

***Added***:

* Support Python 3 ([#2874](https://github.com/DataDog/integrations-core/pull/2874))

## 1.2.1 / 2018-09-04 / Agent 6.5.0

***Fixed***:

* Add data files to the wheel package ([#1727](https://github.com/DataDog/integrations-core/pull/1727))

## 1.2.0 / 2018-05-11

***Added***:

* Adds custom tag support for service check.

***Fixed***:

* Add debug logs and a noisier error message.

## 1.1.1 / 2018-02-13

***Fixed***:

* Checks available metrics for backwards compatibility ([#1066](https://github.com/DataDog/integrations-core/issues/1066))

## 1.1.0 / 2017-08-21

***Added***:

* adds gpu metrics.

## 1.0.0 / 2017-03-22

***Added***:

* adds mesos_slave integration.