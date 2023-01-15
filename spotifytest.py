import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import random


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3a90ccaaa2ed467ca3446c605016e52b",
                                               client_secret="f07b311374724e16b0629a80aba4bd7b",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read user-modify-playback-state user-read-playback-state"))

playlist_id = 'https://open.spotify.com/playlist/2dcuxjUWqSUCiaegmcsIdK?si=8f154920715a49b3'
offset = 0
tracks = []

user_info = sp.current_user()

while True:
    temp_tracks = sp.playlist_items(playlist_id, limit = 100, offset = offset)

    if len(temp_tracks) < 100:
        tracks.append(temp_tracks)
        break
    else:
        tracks.append(temp_tracks)
        offset += 100

track_uris = []
for track in tracks[0]['items']:
    track_uris.append(track['track']['album']['uri'])


song_uri = track_uris[random.randint(0, len(track_uris))]

colour = ["red", "blue", "yellow", "green", "purple"]
while True:
    devices = sp.devices()
    device_list = []

    if (devices['devices'] == []):
        print("\nYou have no spotify apps open at the moment, please open spotify on one of your devices")
        input("Once you have opened spotify, press ENTER to retry...")
    else:
        break

for index, device in enumerate(devices['devices']):
    device_list.append((device['name'], index, device['type'], device['is_active']))

device_found = False

for index, device in enumerate(device_list):
    if (device[3] == True):
        play_device = index
        device_found = True

if (device_found == False) and (len(device_list) > 1):

    print("\nPlease select a device to play music through")
    
    while True:
        print('')

        for index, device in enumerate(device_list):
            print((1+index),'-',device[0])
        
        try:
            play_device = (int(input('Choose a device: ')) - 1)
            
            if (play_device <= len(device_list)):
                break
            else:
                print('Please enter a number listed')
        except ValueError:
            print('Please enter a number listed')

elif (device_found == False):
    play_device = 0
        

sp.start_playback(device_id = ((sp.devices()).get('devices')[play_device]).get('id'), context_uri = song_uri)



