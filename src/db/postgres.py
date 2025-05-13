from peewee import PostgresqlDatabase

__database__ = "application"
__password__ = "123456"
__ip__ = "localhost"
__port__ = "5432"
__user__ = "application"

db = PostgresqlDatabase(f"postgresql://{__user__}:{__password__}@{__ip__}:{__port__}/{__database__}")

