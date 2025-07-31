# Projeto do TCC

## Tecnologias utilizadas
- Python 3.12
- FastAPI
- Peewee
- Dotenv

## Pré-requisitos
- Interpretador [Python](https://www.python.org/downloads/) versão 3.12 ou superior
- Gerenciador de pacotes pip
- Um [ambiente virtual](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) pip

## Como executar:
```bash
git clone https://github.com/gustavoalmeidam7/backend-tcc
cd backend-tcc

pip install -r requirements.txt
```

Copie o arquivo ``` example.env ``` e renomeie o mesmo para ``` .env ``` na raiz do projeto e troque as chaves necessárias, exemplo:
```js
environment = PROD         (Usar "PROD" ou "DEV")
secret_key_jwt = changeme  (Troque para uma secret key segura)
algorithm_jwt= HS256       (Compatível com o algotirimo HS256)

db_database=database           (O database do seu banco de dados postgres)
db_password=secret_db_password (A senha para seu usuário postgres)
db_host=127.0.0.1              (Host ou ip para o database)
db_port=5432                   (A porta do banco, essa é o padrão)
db_user=user                   (Usuário para o banco de dados)
```

A o usar a chave do environment "PROD", você precisa definir todas que iniciam com db_ e ter uma instancia do postgres rodando, se quiser apenas testar usando um banco sqlite você pode apenas mudar a key do environment para "DEV"

Para executar use:
```bash
uvicorn src.main:app
```

## Acessar documentação:
Url padrão para OpenAPI:
```
http://localhost:8000/api/docs
```

Url padrão para Redoc:
```
http://localhost:8000/api/redoc
```
