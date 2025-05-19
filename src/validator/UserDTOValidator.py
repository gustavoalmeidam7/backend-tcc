
class Error():
    def __init__(self, successful: bool = False , message: str = None) -> None:
        self.message = message
        self.successful = successful

class UserDTOValidator:
    def __init__(self, userDTO: 'UserDTO') -> None:
        self.userDTO = userDTO
        self.errors = []

    def validate(self) -> None:
        if not self.userDTO.birthday:
            self.errors.append("Data de nascimento inválida ou não informada!")
        
        if not self.userDTO.email:
            self.errors.append("Email inválido ou não informado!")
        
        if not self.userDTO.phone_number:
            self.errors.append("Telefone inválido ou não informado!")
        
        if not self.userDTO.username:
            self.errors.append("Nome de usuário inválido ou não informado!")
        
        if not self.userDTO.password:
            self.errors.append("Senha inválida ou não informada!")
        
        if not self.userDTO.cpf:
            self.errors.append("CPF inválido ou não informado!")
    
    def was_errors(self) -> bool:
        return len(self.errors) > 0

    def get_errors(self) -> list:
        return self.errors
