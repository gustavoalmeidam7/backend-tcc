from src.db import postgres, sqlite

from ntpath import dirname

from dotenv import load_dotenv

import os

databases = {
    "PROD": postgres.db,
    "DEV" : sqlite.db
}

dotenv_path = dirname(__file__) + "/../../.env"
load_dotenv(dotenv_path)

db = databases[os.environ.get("enviroment")]
