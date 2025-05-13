from peewee import AutoField, ForeignKeyField, Model
from src.domain.User import User
from src.domain.Driver import Driver
from src.db.postgres import db

class Travel(Model):
    travel_id = AutoField()
    user_id = ForeignKeyField(User, backref="travels")
    driver_id = ForeignKeyField(Driver, backref="travels")

    def __repr__(self) -> str:
        return f"<Travel (travel_id={self.travel_id}, user_id={self.user_id}, driver_id={self.driver_id})>"

    class Meta():
        database = db
        db_table = "travel"
