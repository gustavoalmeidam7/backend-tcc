# Projeto do TCC

## Tecnologias utilizadas
- Python 3.12
- Flask/ Flask-restx
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

pip install -r requiriments.txt
```

Crie um arquivo ``` .env ```  na raiz do projeto e coloque a chave:
```js
environment = DEV
```

A chave PROD também pode ser usada, porém é necessario um banco de dados postgres

Finalmente rode:
```bash
python -m src.main
```

## Acessar documentação:
Url padrão:
```
http://localhost:5000/api/doc
```
