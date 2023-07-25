[![Lifecycle:Maturing](https://img.shields.io/badge/Lifecycle-Maturing-007EC6)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)

# DriveBC Load Tests

This repository is for developing and executing load testing scripts against the
[new DriveBC.ca site](https://github.com/bcgov/DriveBC.ca).

- [DriveBC Load Tests](#drivebc-load-tests)
  - [Locust documentation](#locust-documentation)
  - [Usage](#usage)
    - [Examples:](#examples)
      - [WebUI, Single Thread:](#webui-single-thread)
      - [Headless, Single Thread:](#headless-single-thread)
      - [Headless, Distributed](#headless-distributed)
        - [Master Terminal:](#master-terminal)
        - [Worker Terminals (worker number must match the master's --expect-workers value):](#worker-terminals-worker-number-must-match-the-masters---expect-workers-value)

---

## <a name="locustdocs"></a>Locust documentation
[Locust](https://docs.locust.io/en/stable/index.html)

## <a name="usage"></a>Usage

Note that load shaping is being used in the load script, so we don't need to pass in users, spawn rate, or run times. 

Basic CLI command structure:
```bash
locust -f <testfile>.py -H <target URL(:target port)>
```

### Examples:
```bash
locust -f frontend.py -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca
```

#### WebUI, Single Thread:
```bash
locust -f locustfiles -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca
```

#### Headless, Single Thread:
```bash
locust -f locustfiles --headless -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca --html ./reports/frontend_report.html
```

or:
```bash
export TARGET_HOST="https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/"
```
```bash
locust -f locustfiles --headless -H $TARGET_HOST --html ./reports/frontend_report.html
```

#### Headless, Distributed
##### Master Terminal:
```bash
locust -f locustfiles --H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/ --headless --master --expect-workers=8 --html ./reports/frontend_report.html
```

or:
```bash
export TARGET_HOST="https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/"
```
```bash
locust -f locustfiles -H $TARGET_HOST --headless --master --expect-workers=8 --html ./reports/frontend_report.html
```

##### Worker Terminals (worker number must match the master's --expect-workers value):
```bash
locust -f locustfiles --headless --worker
```