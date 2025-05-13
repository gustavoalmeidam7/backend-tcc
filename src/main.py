from src.service.UserService import UserService

from src.dto.CreateUser import *

from src.domain import User, Driver, Travel

from src.db.postgres import db

db.connect()

db.create_tables([User.User, Driver.Driver, Travel.Travel])


userService = UserService()

userService.delete_by_id(5)

print(userService.create(usuario="Gustavin", email="aaaa@mail.com").message)
