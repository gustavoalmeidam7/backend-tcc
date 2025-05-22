from flask_restx import Namespace, fields
from playhouse.shortcuts import model_to_dict
from src.model.User import User

class UserResponseDTO:
    def __init__(
        self, id: int = None, username: str = None, email: str = None
    ) -> None:
        self.id = id
        self.username = username
        self.email = email

    @staticmethod
    def from_model(userModel: User) -> 'UserResponseDTO':
        return UserResponseDTO(
            id           = userModel.id,
            username     = userModel.username,
            email        = userModel.email
        )

    @staticmethod
    def model_to_dict(userModel: 'User') -> dict:
        dictResponse = model_to_dict(userModel)

        keysToRemove = [ 'cpf', 'phone_number', 'password', 'birthday' ]
        for key in keysToRemove:
            if key in dictResponse:
                del dictResponse[key]

        return dictResponse

    def to_model(self) -> User:
        return User(
            id           = self.id,
            username     = self.username,
            email        = self.email
        )

def doc_model(api: Namespace) -> dict:
    return api.model(
        "ResponseUserDTO",
        {
            "id":           fields.Integer(description="Indentificador ID do usuário", example=43),
            "username":     fields.String(description="Nome de usuário", example="Ronaldo de Assis Moreira"),
            "email":        fields.String(description="Email do usuário", example="ronaldinhogaucho@email.com")
        }
    )
