# DriveBC Code Challenge - OXD


## Installation

1. Install Docker and Docker Compose.
2. Clone the project.
3. `cd drivebc-code-challenge`
4. Run `docker-compose up -d --build` to build and start containers.
5. The site should now be is available at <http://localhost:3000>.
6. Visit <http://localhost:8000/admin/> and you should see the Django Admin (admin/admin123).

### Testing Email Notifications

Mailhog SMTP server and local mail client for testing emails is available at <http://localhost:8025>.

### Testing Event Notifications

The app checks for newly added road events that occur along saved routes every 5 minutes. If such events are found, email notifications are sent. They can be checked at <http://localhost:8025>.


## Development Setup (MacOS)

1. Install Docker and Docker Compose.
2. Install [pre-commit](https://pre-commit.com):
   `brew install pre-commit`.
3. Clone the project.
4. `cd drivebc-code-challenge`
5. Set up the pre-commit hooks:
   `pre-commit install && pre-commit install --hook-type commit-msg`.
6. Run `docker-compose up -d --build` to build and start containers.
7. The site should now be is available at <http://localhost:3000>.
    Visit <http://localhost:8000/admin/> (login required) and you
   should see the Django Admin.

A default admin user account for testing purposes is generated with the following credentials (if this username doesn't exist already):

* Username: `admin`
* Password: `admin123`


## Development Setup (Windows)

1. Install Docker and Docker Compose.
2. Install [pre-commit](https://pre-commit.com) _(watch for a message in the console "Scripts is not on PATH" and add it to the environment variable PATH if applicable)_:

   ```
   pip install pre-commit
   ```

3. Clone the project.
4. `cd drivebc-code-challenge`
5. Set up the pre-commit hooks _(ensure the Python Scripts folder is in your path before running this step -- see step #2)_:

   ```
   pre-commit install
   pre-commit install --hook-type commit-msg
   ```

6. Run `docker-compose up -d --build` to build and start containers.
7. The site should now be is available at <http://localhost:3000>.
    Visit <http://localhost:8000/admin/> (login required) and you
    should see the Django Admin.

A default admin user account for testing purposes is generated with the following credentials (if this username doesn't exist already):

* Username: `admin`
* Password: `admin123`


## Docker and Network Architecture

* `drivebc_backend`: Django web app. Restarts on code changes.
* `drivebc_frontend`: React front end.
* `drivebc_db`: Postgres database.
* `drivebc_mailhog`: SMTP server and local mail client for debugging.
* `drivebc_redis`: Redis. Used for caching and task queues.
* `drivebc_worker`: Huey worker (task consumer for jobs like polling for events)


## Application Development

### Coding Style and Conventions

This project uses the [Black code
style](https://black.readthedocs.io/en/stable/the_black_code_style.html).
It also checks syntax, including import order and complexity, via
flake8. Linting is done via pre commit hooks installed using
[pre-commit](https://pre-commit.com).

Javascript linting via eslint is run in a pre commit hook. To set up
Javascript linting in VS Code, install yarn and run `yarn install` in
the `frontend` directory, and install the ESlint extension.

### Security

This project runs vulnerability scans on both the backend and frontend projects.

* `Bandit`: A code analysis tool that checks for security issues in Python code.
* `Safety`: Checks python dependencies for security vulnerabilities.
* `Audit`: Checks javascript dependencies for security vulnerabilities.

NOTE: This current is run manually with `npm audit` but can be added to a build pipeline.

### Git Workflow

Changes should be submitted via a Github PR, and approved by at least
one other dev before merging. We follow the
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) branching model; development branches should be prefixed (e.g.
`feature/`) and merged into the `develop` branch. At release time,
`develop` is merged into `main`, which should track the current
production release.

Merge commits are generally preferred for complex changes, although for
simple (e.g. small single commit) changes fast-forward is OK.

It's not strictly required but the [gitflow-avh
plugin](https://github.com/petervanderdoes/gitflow-avh) makes it much
easier to follow this workflow. See the [gitflow
cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/) for
common operations.


### Running Tests in Docker

`make test` will run python tests via pytest and frontend tests via
jest. You can also run them directly with
`docker-compose run --rm django python -m pytest` (pytest) and
`docker-compose run --rm react yarn test` (jest).

By default, the pytest tests run a reasonable subset of possible
permissions checks. To run tests for most possible permissions cases,
pass the `-m full_perms` argument.

To generate Python test coverage, run `make coverage`. To run type
checks, use `make typecheck`.

By default, tests are run using in memory SQLite.

## Deployment

1. TODO
