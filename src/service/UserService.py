from playhouse.shortcuts import model_to_dict
from src.repository.UserRepository import UserRepository

from src.dto.UserDTO import UserDTO

from src.dto.CreateUser import CreateUserResult, UserStatus

from src.service.Utils import bulk_convert_to_dict

class UserService:
    userRepository = UserRepository()

    def create(self, usuario: str, email: str) -> CreateUserResult:
        if self.userRepository.exists_by_email(email):
            return CreateUserResult(
                status= UserStatus.EXISTS,
                message= "Usuário já existe!"
            ), None

        createdUser = self.userRepository.create(UserDTO(username=usuario, email=email))
        dictResponse = model_to_dict(createdUser)
        result = CreateUserResult(
            status= UserStatus.CREATED,
            message= "Usuário criado com sucesso!"
        )

        return result, dictResponse
    
    def delete_by_id(self, id: int) -> None:
        self.userRepository.delete_by_id(id)

    def delete_all(self) -> None:
        self.userRepository.delete_all()

    def find_all(self) -> dict:
        return bulk_convert_to_dict(self.userRepository.find_all())
