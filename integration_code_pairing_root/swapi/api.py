import requests


BASE_URL = 'https://swapi.dev/api/'


def get_planet_by_id(id):
    url = f'{BASE_URL}planets/{id}/'
    response = requests.get(url)
    
    return response.status_code == 200, response.json()