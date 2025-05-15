from src.model import User


class UserDTO:
    id: int
    username: str
    email: str

    def toModel(self) -> User:
        return User(
            id= self.id,
            username= self.username,
            email= self.id
        )
    
    @staticmethod
    def fromModel(userModel: User):
        return UserDTO(
            id= userModel.id,
            username= userModel.username,
            email= userModel.id
        )

    def __init__(self, id = None, username = None, email = None):
        self.id = id
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"<UserDTO (id={self.id}, username={self.username}, email={self.username})>"
