import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '42299a09c9782f745710fb106afa5a5a'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '28552'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    

def test_part_of_responce():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == "Георгий"

    
@pytest.mark.parametrize('key, value', [('name', 'Георгий'), ('trainer_id', TRAINER_ID), ('id', '282056')])
def test_parametrize(key, value):
        response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
        assert response_parametrize.json()["data"][0][key] == value
