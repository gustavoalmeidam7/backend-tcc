from src.DB import postgres, sqlite

from src.Utils.env import get_env_var

class connection:
    database = "application"
    password = "123456"
    ip = "localhost"
    port = "5432"
    user = "application"

databases = {
    "PROD": postgres.Database(connection),
    "DEV" : sqlite.Database(connection)
}

try:
    get_env_var("environment")
except(KeyError):
    raise RuntimeError("No \"environment\" key set on .env file, please set one (\"PROD\" or \"DEV\")")

db = databases[get_env_var("environment")].db
