from playhouse.shortcuts import model_to_dict
from src.dto.UserDTO import UserDTO
from src.validator.UserDTOValidator import Error, UserDTOValidator
from src.repository.UserRepository import UserRepository

from src.dto.CreateUser import CreateUserResult, UserStatus

from src.service.Utils import bulk_convert_to_dict

class UserService:
    userRepository = UserRepository()

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

        createdUser = self.userRepository.create(userDTO.toModel())

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
