import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cfb0ff184151ae098bd193e20522f8d7'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '36858'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '36858'
    
@pytest.mark.parametrize('key, value', {('trainer_name', 'Владимир'), ('id', TRAINER_ID)})
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value