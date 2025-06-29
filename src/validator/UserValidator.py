from src.model.User import User
from src.repository.UserRepository import UserRepository

userRepository = UserRepository()

def is_user_valid(userModel: User) -> 'bool':
    isEmailUnique = is_email_unique(userModel.email)
    isPhoneNumberUnique = is_phone_number_unique(userModel.phone_number)
    isCpfUnique = is_cpf_unique(userModel.cpf)

    return (isEmailUnique and isPhoneNumberUnique and isCpfUnique)

def is_email_unique(email: str) -> 'str':
    return not userRepository.exists_by_email(email)

def is_phone_number_unique(phone_number: str) -> 'str':
    return not userRepository.exists_by_phone_number(phone_number)

def is_cpf_unique(cpf: str) -> 'str':
    return not userRepository.exists_by_cpf(cpf)
