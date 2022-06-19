# StatusService


Start a project with:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up
```

If you want to develop in docker with autoreload, use this command:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up
```

This command exposes application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```


## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

## Migrations

If you want to migrate your database, you should run following commands:
```bash
# Upgrade database to the last migration.
aerich upgrade
```

### Reverting migrations

If you want to revert migrations, you should run:
```bash
aerich downgrade
```

### Migration generation

To generate migrations you should run:
```bash
aerich migrate
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . run --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=StatusService" -e "POSTGRES_USER=StatusService" -e "POSTGRES_DB=StatusService" postgres:13.6-bullseye
```


2. Run the pytest.
```bash
pytest -vv .
```
