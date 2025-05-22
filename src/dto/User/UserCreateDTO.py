import datetime

from src.model.User import User

from flask_restx import fields, Namespace

from src.service.Utils import unmask_number

class UserDTO:
    def __init__(
        self, username: str = None, cpf: str = None,
        birthday: datetime = None, email: str = None, phone_number: str = None, password: str = None
    ) -> None:
        self.username = username
        self.cpf = cpf
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number
        self.password = password

    @staticmethod
    def from_dict(userJson: dict
    ) -> 'UserDTO':

        user_birthday = None

        if userJson.get("birthday"):
            user_birthday = datetime.datetime.strptime(userJson.get("birthday"), '%d-%m-%Y').date()

        return UserDTO(
            username     = userJson.get("username"),
            cpf          = unmask_number(userJson.get("cpf")),
            birthday     = user_birthday,
            email        = userJson.get("email"),
            phone_number = unmask_number(userJson.get("phone_number")),
            password     = userJson.get("password")
        )

    @staticmethod
    def from_model(userModel: User) -> 'UserDTO':
        return UserDTO(
            username     = userModel.username,
            cpf          = userModel.cpf,
            birthday     = userModel.birthday,
            email        = userModel.email,
            phone_number = userModel.phone_number,
            password     = userModel.password
        )

    def to_model(self) -> User:
        return User(
            username=self.username,
            cpf=self.cpf,
            birthday=self.birthday,
            email=self.email,
            phone_number=self.phone_number,
            password=self.password
        )

def doc_model(api: Namespace) -> dict:
    return api.model(
        "CreateUserDTO",
        {
            "username":     fields.String(required=True, description="Nome de usuário", example="Ronaldo de Assis Moreira"),
            "cpf":          fields.String(required=True, description="CPF do usuário", example="12345678900"),
            "birthday":     fields.Date  (required=True, description="Data de nascimento do usuário", example="21-05-1980"),
            "email":        fields.String(required=True, description="Email do usuário", example="ronaldinhogaucho@email.com"),
            "phone_number": fields.String(required=True, description="Número de telefone do usuário", example="55511234567"),
            "password":     fields.String(required=True, description="Senha do usuário", example="senhasegur@1234"),
        }
    )
