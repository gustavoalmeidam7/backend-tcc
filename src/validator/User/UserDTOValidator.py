from src.repository.UserRepository import UserRepository


class Error():
    def __init__(self, name: str = "erro", message: str = None) -> None:
        self.name = name
        self.message = message

class UserDTOValidator:
    def __init__(self, userDTO: 'UserDTO') -> None:
        self.userDTO = userDTO
        self.repository = UserRepository()
        self.errors = []

    def validate(self) -> None:
        if self.repository.exists_by_cpf(self.userDTO.cpf):
            self.errors.append(Error("cpf already exists", "CPF já cadastrado!"))

        if self.repository.exists_by_phone_number(self.userDTO.phone_number):
            self.errors.append(Error("phone_number already exists", "Telefone já cadastrado!"))
        
        if self.repository.exists_by_email(self.userDTO.email):
            self.errors.append(Error("email already exists","Email já cadastrado!"))

        if not self.userDTO.birthday:
            self.errors.append(Error("birthday is null","Data de nascimento não informada!"))
        
        if not self.userDTO.email:
            self.errors.append(Error("email is null","Email inválido ou não informado!"))
        
        if not self.userDTO.phone_number:
            self.errors.append(Error("phone_number is null","Telefone inválido ou não informado!"))
        
        if not self.userDTO.username:
            self.errors.append(Error("username is null","Nome de usuário inválido ou não informado!"))
        
        if not self.userDTO.password:
            self.errors.append(Error("password is null","Senha inválida ou não informada!"))
        
        if not self.userDTO.cpf:
            self.errors.append(Error("cpf is null","CPF inválido ou não informado!"))
    
    def was_errors(self) -> bool:
        return len(self.errors) > 0

    def get_errors(self) -> list:
        return self.errors
