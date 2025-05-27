from playhouse.shortcuts import model_to_dict
from src.dto.User.UserResponseDTO import UserResponseDTO
from src.dto.User.UserCreateDTO import UserDTO
from src.validator.User.UserDTOValidator import Error, UserDTOValidator
from src.repository.UserRepository import UserRepository

from src.dto.User.CreateUser import CreateUserResult, UserStatus

class UserService:
    instance = None

    userRepository = UserRepository.get_instance()

    @staticmethod
    def get_instance() -> 'UserRepository':
        if not UserService.instance:
            UserService.instance = UserRepository()
        return UserService.instance

    #TODO validar se o cpf é válido e mascara
    #TODO mascara do email 
    #TODO mascara do telefone
    def create(self, userDTO: UserDTO) -> CreateUserResult:
        userDTOValidator = UserDTOValidator(userDTO)
        userDTOValidator.validate()

        if userDTOValidator.was_errors():
            errors = userDTOValidator.get_errors()
            dict_errors = []
            for error in errors:
                dict_errors.append({error.name: error.message})

            return CreateUserResult(
                status= UserStatus.INVALID,
                message= dict_errors
            ), None

        createdUser = self.userRepository.create(userDTO.to_model())

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

    def find_all_page_dict(self, page: int = 0, pagesize: int = 25) -> dict:
        page = page or 1        # Tranforma page em 1 se o valor for None ou 0
        pagesize = pagesize or 1

        pagesize = max(1, min(pagesize, 50))
        page = max(1, page)

        return list(map(UserResponseDTO.model_to_dict, self.userRepository.find_all_with_page(page, pagesize)))
    
