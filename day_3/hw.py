# making an API call
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if r.status_code == 200:
    data = r.json()

print(data.keys())


