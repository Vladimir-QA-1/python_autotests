import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'тут токен тренера'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 9
}

body_rename = {
    "pokemon_id": "id покемона",
    "name": "paper",
    "photo_id": 1000
}

body_add_pokeboll = {
    "pokemon_id": "id покемона"
}

r'''esponse_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

'''response_add_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeboll)
print(response_add_pokeboll.text)'''

message = response_rename.json()['message']
print(message)
