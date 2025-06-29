from src.schema.User.UserCreateSchema import UserCreateSchema
from src.schema.User.UserResponseSchema import UserResponseSchema

from src.validator.UserValidator import is_user_valid
from fastapi import HTTPException

from src.repository.UserRepository import UserRepository
from src.utils.singleton import singleton

@singleton
class UserService:
    userRepository = UserRepository()

    def create(self, userSchema: UserCreateSchema) -> 'UserResponseSchema':
        userModel = userSchema.to_model()
        if(not is_user_valid(userModel)):
            raise HTTPException(status_code=400 ,detail="Email, Phone Number ou CPF já existem") # TODO Arrumar status code e código de erro


        createdUser = self.userRepository.create(userSchema.to_model())

        return UserResponseSchema.from_user_model(createdUser)
    
    def delete_by_id(self, id: int) -> None:
        self.userRepository.delete_by_id(id)

    def delete_all(self) -> None:
        self.userRepository.delete_all()

    def find_all_page_dict(self, page: int = 0, pagesize: int = 25) -> 'list[UserResponseSchema]':
        page = page or 1        # Transforma page em 1 se o valor for None ou 0
        pagesize = pagesize or 1

        pagesize = max(1, min(pagesize, 50))
        page = max(1, page)

        return list(map(UserResponseSchema.from_user_model, self.userRepository.find_all_with_page(page, pagesize)))
    
