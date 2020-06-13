import requests 

URL = "https://swapi.dev/api/people/1/"

r = requests.get(url = URL)

data = r.json()

print(data)
