import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3a90ccaaa2ed467ca3446c605016e52b",
                                               client_secret="f07b311374724e16b0629a80aba4bd7b",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read user-modify-playback-state user-read-playback-state"))

playlist_id = 'https://open.spotify.com/playlist/0tnsqKhnn7rKAD7sevyRU2?si=b207536b74584497'
offset = 0
tracks = []

user_info = sp.current_user()

while True:
    temp_tracks = sp.playlist_items(playlist_id, limit = 100, offset = offset)
    #print(temp_tracks)
    if len(temp_tracks) < 100:
        tracks.append(temp_tracks)
        break
    else:
        tracks.append(temp_tracks)
        offset += 100


for track in tracks[0]['items']:
    print(track['track']['album']['name'],'\t\t\t\t',track['track']['album']['id'])
song_id = "6Hmc5Afutf4hcrjnBYNidS?"
colour = ["red", "blue", "yellow", "green", "purple"]

#sp.add_to_queue(song_id, ((sp.devices()).get('devices')[0]).get('id'))
#sp.next_track()



# results = sp.current_user_saved_tracks(10, 0)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])



