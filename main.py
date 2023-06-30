from get_the_lyrics import Lyrics
from find_path import Path
from spotify_connection import ConnectWithSpotify

choice = input("Co chciał byś zrobić:"
               "\n1. Zobaczyć tekst konkretnego utworu."
               "\n2. Wyświetlać nabierząco text utworów ze Spotify."
               "\nWybór: ")

if choice == "1":
    song = Path()
    path = song.search_the_song()
    lyrics = Lyrics(path)
    print(lyrics.lyrics())
elif choice == "2":
    song = ConnectWithSpotify()
    song.get_token()
    song.connection()
else:
    print("Nie rozumiem polecenia")
