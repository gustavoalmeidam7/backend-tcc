from collections import UserList
from src.model.User import User
from src.dto.UserDTO import UserDTO
from playhouse.shortcuts import model_to_dict

class UserRepository:
    def create(self, userDto: UserDTO) -> None:
        return User.create(
            username = userDto.username,
            email = userDto.email
        )

    def find_by_id(self, id: int) -> UserDTO:
        return User.get(User.id == id).toDto()

    def find_all(self) -> UserList:
        return list(User.select())

    def update(self, userDto: UserDTO) -> None:
        query = User.update(id=userDto.id, username=userDto.username, email=userDto.email).where(User.id == userDto.id)
        query.execute()

    def delete_by_id(self, id: int) -> None:
        User.delete_by_id(id)

    def delete_all(self) -> None:
        User.delete().where(User.select())

    def exists_by_id(self, id: int) -> bool:
        return User.select().where(User.id == id).exists()

    def count(self) -> int:
        return User.select().count()

    def find_by_email(self, email: str) -> UserDTO:
        return User.get(User.email == email).toDto()
    
    def exists_by_email(self, email: str) -> bool:
        return User.select().where(User.email == email).exists()
