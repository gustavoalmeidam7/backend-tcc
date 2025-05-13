from src.model import User, Driver, Travel

from src.db.postgres import db

from src.controller import Controller

def main():
    db.connect()

    db.create_tables([User.User, Driver.Driver, Travel.Travel])

    Controller.init()

if __name__ == "__main__":
    main()
