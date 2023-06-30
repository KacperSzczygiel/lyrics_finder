from get_the_lyrics import LyricsParser
from find_path import Path
from spotify_connection import SpotifyConnection


class Handler:
    @staticmethod
    def choice():
        choice = input("Option:"
                       "\n1. Show the lyrics of specific song."
                       "\n2. Display current playing song from Spotify."
                       "\nYour choice: ")
        return choice

    def handler(self):
        result = self.choice()
        if result == "1":
            path = Path()
            song = path.get_path()
            lyrics = LyricsParser(song)
            print(lyrics.parse_lyrics())
        elif result == "2":
            song = SpotifyConnection()
            song.get_token()
            song.connection()
        else:
            print("I do not understand your command")
