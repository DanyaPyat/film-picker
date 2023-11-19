import requests
import json

url = "https://imdb188.p.rapidapi.com/api/v1/searchIMDB"

querystring = {"query": "openheimer"}

headers = {
    "X-RapidAPI-Key": "b4f10612f7msh1d2976320187102p1c09dcjsn12e5eee2a4d5",
    "X-RapidAPI-Host": "imdb188.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

with open("sample.json", "w") as outfile:
    outfile.write(json.dumps(response.json(), indent=2))
