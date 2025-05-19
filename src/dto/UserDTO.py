import datetime

from src.model.User import User

class UserDTO:
    def __init__(
        self, username: str, cpf: str,
        birthday: datetime, email: str, phone_number: str, password: str
    ) -> None:
        self.username = username
        self.cpf = cpf
        self.birthday = birthday
        self.email = email
        self.phone_number = phone_number
        self.password = password

    @staticmethod
    def fromDict(userJson: dict
    ) -> 'UserDTO':
        if not userJson:
            raise ValueError("User JSON cannot be None")

        #TODO melhor checagem na service, ainda fazendo passar daqui para ser validade email e etc
        if not userJson["birthday"]:
            raise ValueError("User birthday cannot be None")

        return UserDTO(
            username     = userJson["username"],
            cpf          = userJson["cpf"],
            birthday     = datetime.datetime.strptime(userJson["birthday"], '%d-%m-%Y').date(),
            email        = userJson["email"],
            phone_number = userJson["phone_number"],
            password     = userJson["password"]
        )

    @staticmethod
    def fromModel(userModel: User) -> 'UserDTO':
        return UserDTO(
            username     = userModel.username,
            cpf          = userModel.cpf,
            birthday     = userModel.birthday,
            email        = userModel.email,
            phone_number = userModel.phone_number,
            password     = userModel.password
        )

    def toModel(self) -> User:
        return User(
            username=self.username,
            cpf=self.cpf,
            birthday=self.birthday,
            email=self.email,
            phone_number=self.phone_number,
            password=self.password
        )

    
