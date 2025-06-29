from src.model import User, Driver, Travel

from src.controller import app
from src.controller.UserController import userRouter

from src.db.DB import db

@app.on_event("startup")
def main():
    db.connect()
    db.create_tables([User.User, Driver.Driver, Travel.Travel])
    app.include_router(userRouter)

