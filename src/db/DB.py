from src.db import postgres, sqlite

from ntpath import dirname

from dotenv import load_dotenv

import os

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

dotenv_path = dirname(__file__) + "/../../.env"
load_dotenv(dotenv_path)

try:
    os.environ.get("enviroment")
except(KeyError):
    raise RuntimeError("No \"enviroment\" key set on .env file, please set one (\"PROD\" or \"DEV\")")

db = databases[os.environ.get("enviroment")].db
