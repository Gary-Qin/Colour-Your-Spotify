import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# $env:SPOTIPY_CLIENT_ID='94999ad051a24821989fc2b351ece004'
# $env:SPOTIPY_CLIENT_SECRET='a642a27e5fd04cbe80e6512c41ae804a'
# $env:SPOTIPY_REDIRECT_URI='http://google.com/'

scope = "user-library-read user-modify-playback-state user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="94999ad051a24821989fc2b351ece004",
                                               client_secret="a642a27e5fd04cbe80e6512c41ae804a",
                                               redirect_uri="http://google.com/",
                                               scope=scope))
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

song_id = "6Hmc5Afutf4hcrjnBYNidS?"
colour = ["red", "blue", "yellow", "green", "purple"]

sp.add_to_queue(song_id, ((sp.devices()).get('devices')[0]).get('id'))
sp.next_track()
print(sp.playlist_tracks("https://open.spotify.com/playlist/0urovHBAaGIhu1HNTcb1mv?si=18503fc027494715", "spotify", 1))    


# results = sp.current_user_saved_tracks(10, 0)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])



