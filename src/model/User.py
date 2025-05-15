from peewee import Model, AutoField, CharField
from src.db.DB import db

from src.dto.UserDTO import UserDTO

class User(Model):
    id = AutoField(primary_key=True)
    username = CharField()
    email = CharField(unique=True)

    def toDto(self) -> UserDTO:
        return UserDTO(
            id= self.id,
            username= self.username,
            email= self.id
        )
    
    @staticmethod
    def fromDto(userDTO: UserDTO):
        return User(
            id= userDTO.id,
            username= userDTO.username,
            email= userDTO.id
        )

    def __repr__(self) -> str:
        return f"<User (id={self.id}, username={self.username}, email={self.username})>"

    class Meta():
        database = db
        db_table = "users"
