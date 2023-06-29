from bs4 import BeautifulSoup
import requests
import re


class Lyrics:
    def __init__(self, path):
        self.path = path

    def lyrics(self):
        page = requests.get("https://genius.com" + self.path)
        soup = BeautifulSoup(page.text, 'html.parser')
        div = soup.find(class_="Lyrics__Container-sc-1ynbvzw-5 Dzxov")
        for br in div.find_all("br"):
            br.replace_with("\n")
        lyrics = re.sub('<[^<]+?>', '', str(div))
        return lyrics
