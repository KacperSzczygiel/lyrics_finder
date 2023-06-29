from pprint import pprint
import requests
import json

# name = input("Wpisz nazwę utworu, bądź artysty: ")

params = {
    "client_id:": "zcBdtGYUjGLXuoUtcr0Gfe3WyTl9lOjoYsZHqLu9uGylOHnDuo2dvfUa7mfZp0fb",
    "client_secret": "vXro5SAhey2kD85II9KxUVsBaaabXz2cv8hJEHPg_uwJqzy6DGcGC_2SbiF576V9VfK86HAt3lPJMKJGZyni6Q",
    "access_token": "n7662RkbzNvb5TD8g3hwohLEW264nnYvr9J65iianH46QjPXFbOCezLBYW3mVegI",
    "q": "Malik Montana"  #name
}

login_request = requests.get("https://api.genius.com/search", params)
try:
    content = login_request.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    x = 0
    top_10_songs = {}
    while x < 10:
        song_name = content['response']['hits'][x]['result']['full_title']
        print(str(x + 1) + ".", song_name.replace("\xa0", " "))
        top_10_songs[x + 1] = song_name
        x += 1
