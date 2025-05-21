import datetime

from src.model.User import User

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
            cpf          = userJson.get("cpf"),
            birthday     = user_birthday,
            email        = userJson.get("email"),
            phone_number = userJson.get("phone_number"),
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
