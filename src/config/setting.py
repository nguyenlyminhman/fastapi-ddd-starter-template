from starlette.config import Config
# from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "FastApi DDD"

config = Config(".env")
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
ENV: str = config("ENV", cast=str, default='local')

USER_SERVICE_URL: str = config('USER_SERVICE_URL', cast=str, default='')
JWT_SECRET: str = config('JWT_SECRET', cast=str, default='')
PSQL_USER: str = config('PSQL_USER', cast=str, default='postgres')
PSQL_PASSWORD: str = config('PSQL_PASSWORD', cast=str, default='')
PSQL_HOST: str = config('PSQL_HOST', cast=str, default='localhost')
PSQL_PORT: str = config('PSQL_PORT', cast=str, default='5432')
PSQL_DATABASE: str = config('PSQL_DATABASE', cast=str, default='postgres')

DB_URL: str = "postgres://" + PSQL_USER + ":" + PSQL_PASSWORD + \
    "@" + PSQL_HOST + ":" + PSQL_PORT + "/" + PSQL_DATABASE

REDIS_WRITER: str = config('REDIS_WRITER', cast=str, default='')

ES_URL: str = config('ES_URL', cast=str, default='')
ES_USER: str = config("ES_USER", cast=str, default='')
ES_PASSWORD: str = config("ES_PASSWORD", cast=str, default='')
