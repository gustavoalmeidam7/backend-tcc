from typing import Annotated
from pydantic import BaseModel, Field, AfterValidator, EmailStr

from datetime import date

from src.service.Utils import validate_birthday

from src.model.User import User

class UserResponseSchema(BaseModel):
    username: Annotated[str, Field(max_length=35)]
    birthday: Annotated[date, Field(), AfterValidator(validate_birthday)]
    email:    Annotated[EmailStr, Field(data="email", max_length=45)]

    @staticmethod
    def from_user_model(user: User) -> 'UserResponseSchema':
        return UserResponseSchema(
            username=user.username,
            birthday=user.birthday,
            email=user.email
        )
