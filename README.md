# DriveBC Code Challenge - OXD


## User Authentication
=======

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
8. Run `docker-compose run --rm django python manage.py createsuperuser` and
   follow the prompts to create a superuser with admin access.
   Use their username and password to access Django Admin.

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
8. Run `docker-compose run --rm django python manage.py createsuperuser` and
   follow the prompts to create a superuser with admin access.
   Use their username and password to access Django Admin.

## Docker and Network Architecture
- `drivebc-code-challenge_django_1`: Django web app. Restarts on code changes.
- `drivebc-code-challenge_react_1`: React front end.
- `drivebc-code-challenge_db_1`: Postgres database.

## Application Development


### Makefile Shortcuts

A number of common commands are aliased in `make`; run `make help` for
details.


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
- `Bandit`: A code analysis tool that checks for security issues in Python code.
- `Safety`: Checks python dependencies for security vulnerabilities.
- `Audit`: Checks javascript dependencies for security vulnerabilities. NOTE: This
current is run manually with `npm audit` but can be added to a build pipeline.


### Git Workflow

Changes should be submitted via a Github PR, and approved by at least
one other dev before merging. We follow the
[gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
branching model; development branches should be prefixed (e.g.
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
