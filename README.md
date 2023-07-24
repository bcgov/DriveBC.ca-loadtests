[![Lifecycle:Maturing](https://img.shields.io/badge/Lifecycle-Maturing-007EC6)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)

# DriveBC Load Tests

This repository is for developing and executing load testing scripts against the
[new DriveBC.ca site](https://github.com/bcgov/DriveBC.ca).

- [DriveBC Load Tests](#drivebc-load-tests)
  - [Locust documentation](#locust-documentation)
  - [Usage](#usage)
    - [Examples:](#examples)
      - [WebUI (single):](#webui-single)
      - [Headless (single):](#headless-single)
      - [WebUI (master - workers)](#webui-master---workers)
        - [Master Terminal:](#master-terminal)
        - [Worker Terminals:](#worker-terminals)

---

## <a name="locustdocs"></a>Locust documentation
[Locust](https://docs.locust.io/en/stable/index.html)

## <a name="usage"></a>Usage
Basic CLI command structure:
```bash
locust -f <testfile>.py -H <target URL(:target port)>
```

### Examples:
```bash
locust -f frontend.py -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca
```

#### WebUI (single):
```bash
locust -f locustfiles --users 1000 --spawn-rate 1 -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca
```

#### Headless (single):
```bash
locust -f locustfiles --headless --users 1000 --spawn-rate 1 -t 2m -H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca --html ./reports/frontend_report.html
```

or:
```bash
export TARGET_HOST="https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/"
```
```bash
locust -f locustfiles --headless --users 1000 --spawn-rate 1 -t 2m -H $TARGET_HOST --html ./reports/frontend_report.html
```

#### WebUI (master - workers)
##### Master Terminal:
```bash
locust -f locustfiles --H https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/ --headless --master --expect-workers=1 -u 1000 -r 1 -t 20 --html ./reports/frontend_report.html
```

or:
```bash
export TARGET_HOST="https://drivebc-frontend-c59ecc-test.apps.silver.devops.gov.bc.ca/"
```
```bash
locust -f locustfiles -H $TARGET_HOST --headless --master --expect-workers=1 -u 1000 -r 1 -t 20 --html ./reports/frontend_report.html
```

##### Worker Terminals:
```bash
locust -f locustfiles --headless --worker -u 1000 -r 1
```