from dotenv import load_dotenv
import lyricsgenius as lg
import spotipy
import time
import os

load_dotenv("env.py")


class SpotifyConnection:
    def __init__(self):
        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.url = os.getenv("SPOTIPY_REDIRECT_URL")
        self.access_token = os.getenv("GENIUS_ACCESS_TOKEN")
        self.scope = "user-read-currently-playing"
        self.spotify_object = None
        self.genius = None

    def get_token(self):
        oauth_object = spotipy.SpotifyOAuth(self.client_id, self.client_secret, self.url, scope=self.scope)
        token_dict = oauth_object.get_cached_token()['access_token']
        token = token_dict
        return token

    def connect(self):
        token = self.get_token()
        self.spotify_object = spotipy.Spotify(auth=token)
        self.genius = lg.Genius(self.access_token)

    def get_currently_playing(self):
        return self.spotify_object.currently_playing()

    def get_lyrics(self, title, artist):
        song = self.genius.search_song(title=title, artist=artist)
        if song is not None:
            return song.lyrics
        return None

    def connection(self):
        self.connect()

        while True:
            current = self.get_currently_playing()
            if current is not None:
                status = current['currently_playing_type']
                if status == "track":
                    artist_name = current['item']['album']['artists'][0]['name']
                    song_title = current['item']['name']
                    length = current['item']['duration_ms']
                    progress = current['progress_ms']
                    time_left = int(((length - progress) / 1000))

                    lyrics = self.get_lyrics(song_title, artist_name)
                    if lyrics is not None:
                        print(f"{lyrics}\n\n\n")

                    time.sleep(time_left)
                elif status == "ad":
                    time.sleep(30)
            else:
                time.sleep(5)
