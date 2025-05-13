from peewee import Model, AutoField, CharField, ForeignKeyField
from src.db.postgres import db

class Driver(Model):
    id = AutoField(primary_key=True)
    driver_name = CharField()
    email = CharField(unique=True)
    # ambulance = ForeignKeyField()

    def __repr__(self) -> str:
        return f"<Travel (id={self.id}, driver_name={self.driver_name}, email={self.email})>"

    class Meta():
        database = db
        db_table = "driver"
