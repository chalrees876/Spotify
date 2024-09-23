import spotipy

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

name = ""

results = sp.search(q="shows:" + "Slow Burn", type="show")
items = results['shows']['items']
for item in items:
    print(item['name'])