from fastapi import FastAPI

from dotenv import load_dotenv
import os

load_dotenv()
isDebug = os.getenv("Environment") == "DEV"

app = FastAPI(debug=isDebug, title="Gerenciamento de ambulância API", description="Api para gerenciamento de ambulâncias - TCC", version="1.0.0", docs_url="/docs")
