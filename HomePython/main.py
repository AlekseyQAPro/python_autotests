import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '42299a09c9782f745710fb106afa5a5a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Георгий",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "242825",
    "name": "Василий",
    "photo_id": 6
}
body_addpokeball = {
    "pokemon_id": "242825"
}



response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_create)
print(response_create.text)
pokemon_id = response_create.json()['id']
print(pokemon_id)

response_change = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = body_change)
print(response_change.text)
pokemon_change = response_change.json()['message']
print(pokemon_change)

response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER,json = body_addpokeball)
print(response_addpokeball.text)
add_pokeball = response_addpokeball.json('message')
print(add_pokeball)