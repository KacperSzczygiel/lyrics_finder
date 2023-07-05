from dotenv import load_dotenv
import os
import spotipy

load_dotenv("env.py")

cache_file = ".cache"

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
url = os.getenv("SPOTIPY_REDIRECT_URL")

scope = "user-read-currently-playing"

oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, url, scope=scope)

if os.path.exists(cache_file):
    print("Cache file exist.")
else:
    token = oauth_object.get_access_token()
    print(token)
