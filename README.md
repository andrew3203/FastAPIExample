### First Build Only
1. `cp .env.example .env`
2. `docker network create app_main`
3. `docker-compose up -d --build`

### Linters
Format the code with `ruff --fix` and black
```shell
docker compose exec app format
```

### Migrations
- Create an automatic migration from changes in `src/database.py`
```shell
docker compose exec app makemigrations *migration_name*
```
- Run migrations
```shell
docker compose exec app migrate
```
- Downgrade migrations
```shell
docker compose exec app downgrade -1  # or -2 or base or hash of the migration
```
### Tests
All tests are integrational and require DB connection. 

One of the choices I've made is to use default database (`postgres`), separated from app's `app` database.
- Using default database makes it easier to run tests in CI/CD environments, since there is no need to setup additional databases
- Tests are run with upgrading & downgrading alembic migrations. It's not perfect, but works fine. 

Run tests
```shell
docker compose exec app pytest
```
