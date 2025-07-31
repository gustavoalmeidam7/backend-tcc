from src.DB import postgres, sqlite

from src.Utils.env import get_env_var

class connection:
    database = get_env_var("db_database")
    password = get_env_var("db_password")
    ip       = get_env_var("db_host")
    port     = get_env_var("db_port") or "5432"
    user     = get_env_var("db_user")

databases = {
    "PROD": postgres.Database(connection),
    "DEV" : sqlite.Database(connection)
}

try:
    get_env_var("environment")
except(KeyError):
    raise RuntimeError("Sem chaves de \"environment\" fornecidas no .env file, por favor adicione alguma (\"PROD\" ou \"DEV\")")

db = databases[get_env_var("environment")].db
