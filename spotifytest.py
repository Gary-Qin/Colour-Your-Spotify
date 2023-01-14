import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# $env:SPOTIPY_CLIENT_ID='94999ad051a24821989fc2b351ece004'
# $env:SPOTIPY_CLIENT_SECRET='a642a27e5fd04cbe80e6512c41ae804a'
# $env:SPOTIPY_REDIRECT_URI='http://google.com/'

scope = "user-library-read user-modify-playback-state user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# results = sp.current_user_saved_tracks(10, 0)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
sp.volume(100)
sp.add_to_queue("4CzhtKifG867Lu5DNQVBSA")
sp.next_track()
