from fordev.generators import people
import requests

URL = "http://localhost:5000/api/user/create"

def create_people(number: int = 1) -> 'list[dict]':
    listUsers = []
    for i in range(number):
        person = people()

        nascimento = person[0]["data_nasc"].split("/")
        nascimento = f"{nascimento[0]}-{nascimento[1]}-{nascimento[2]}"
        listUsers.append({
            "username": person[0]["nome"],
            "cpf": person[0]["cpf"],
            "birthday": nascimento,
            "email": person[0]["email"],
            "phone_number": person[0]["celular"],
            "password": person[0]["senha"]
        })

    return listUsers

def insert_users(number: int = 1) -> str :
    users = create_people(number)

    users_created = []
    for user in users:
        content = requests.post(
                URL,
                json=user
            )

        users_created.append(
            content.text
        )
        
    return users_created

nUsers = input("How much users will be generated: ")

print(insert_users(int(nUsers)))
