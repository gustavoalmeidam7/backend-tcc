from src.repository.UserRepository import UserRepository

from src.model.User import User
from src.dto.UserDTO import UserDTO

from src.dto.CreateUser import CreateUserResult, UserStatus

class UserService:
    userRepository = UserRepository()

    def create(self, usuario: str, email: str) -> CreateUserResult:
        if self.userRepository.exists_by_email(email):
            print(self.userRepository.find_by_email(email).id)
            return CreateUserResult(
                status= UserStatus.EXISTS,
                message= "O usuário já existe!"
            )

        self.userRepository.create(UserDTO(username=usuario, email=email))
        return CreateUserResult(
            status= UserStatus.CREATED,
            message= "Usuário criado com sucesso!"
        )
    
    def delete_by_id(self, id: int) -> None:
        self.userRepository.delete_by_id(id)

    def delete_all(self) -> None:
        self.userRepository.delete_all()
