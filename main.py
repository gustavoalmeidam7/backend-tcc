from peewee import PostgresqlDatabase, Model, CharField, IntegerField

db = PostgresqlDatabase(
    database='db',
    user='postgres',
    host='127.0.0.1',
    port=5432
)

class BaseModel(Model):
    class Meta:
        database = db

class Post(BaseModel):
    title = CharField()
    content = CharField()
    views = IntegerField()

db.connect()
db.create_tables([Post])

novo_post = Post.create(title='Meu primeiro post', content='Conteúdo aqui...', views=0)

for post in Post.select():
    print(post.title, post.content, post.views)
