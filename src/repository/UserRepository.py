from src.model.User import User

class UserRepository:
    def create(self, userModel: User) -> User:
        userModel.save(force_insert=True)
        return userModel

    def find_by_id(self, id: int) -> User:
        return User.get(User.id == id)

    def find_all(self) -> 'list[User]':
        return list(User.select())

    def update(self, userModel: User) -> None:
        query = User.update(id=userModel.id, username=userModel.username, email=userModel.email).where(User.id == userModel.id)
        query.execute()

    def delete_by_id(self, id: int) -> None:
        User.delete_by_id(id)

    def delete_all(self) -> None:
        User.delete().where(User.select())

    def exists_by_id(self, id: int) -> bool:
        return User.select().where(User.id == id).exists()

    def count(self) -> int:
        return User.select().count()

    def find_by_email(self, email: str) -> User:
        return User.get(User.email == email).toDto()

    def find_by_cpf(self, cpf: str) -> User:
        return User.get(User.cpf == cpf).toDto()
    
    def exists_by_email(self, email: str) -> bool:
        return User.select().where(User.email == email).exists()

    def exists_by_phone_number(self, phone_number: str) -> bool:
        return User.select().where(User.phone_number == phone_number).exists()

    def exists_by_cpf(self, cpf: str) -> bool:
        return User.select().where(User.cpf == cpf).exists()
