import requests
import json


class Path:
    def __init__(self, client_id, client_secret, access_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    @staticmethod
    def get_search_results(params):
        search_request = requests.get("https://api.genius.com/search", params)
        try:
            content = search_request.json()
        except json.decoder.JSONDecodeError:
            print("Niepoprawny format")
        else:
            return content

    def params(self, name):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "access_token": self.access_token,
            "q": name
        }
        return params

    def search_song(self):
        name = input("Podaj nazwę utworu/artysty: ")
        param = self.params(name)
        content = self.get_search_results(param)
        x = 0
        top_10_songs = {}
        while x < 10:
            song_name = content['response']['hits'][x]['result']['full_title']
            print(str(x + 1) + ".", song_name.replace("\xa0", " "))
            top_10_songs[x + 1] = song_name
            x += 1
        song_index = input("Wybierz index piosenki: ")
        name = top_10_songs[int(song_index)]
        param = self.params(name)
        content = self.get_search_results(param)
        return content['response']['hits'][0]['result']['path']
