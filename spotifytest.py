import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import random
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
import webcolors

image_directory = input("Please paste the directory of the image you would like to use: ")
ct = ColorThief(image_directory)

colors = {'#1772e0': 'blue', '#36e912': 'green', '#871bbe': 'purple', '#c82323': 'red', '#e9e212': 'yellow'}
dominant_color = ct.get_color(quality=1)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3a90ccaaa2ed467ca3446c605016e52b",
                                               client_secret="f07b311374724e16b0629a80aba4bd7b",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read user-modify-playback-state user-read-playback-state"))

playlist_id = ''
offset = 0
tracks = []

user_info = sp.current_user()

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in colors.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                         (g - rgb[1]) ** 2,
                         (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

try:
    cname = webcolors.rgb_to_name(dominant_color)
    print(f"The dominant color is {cname}")
except ValueError:
    cname = closest_color(dominant_color)
    print(f"The dominant color is most likely {cname}")

if cname == "blue":
    playlist_id = "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR?si=577ce2ed756e4ddc"
elif cname == "green":
    playlist_id = "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC?si=c5055c8e13364d7e"
elif cname == "purple":
    playlist_id = "https://open.spotify.com/playlist/37i9dQZF1DX2WkIBRaChxW?si=f5fd0990d75146b3"
elif cname == "red":
    playlist_id = "https://open.spotify.com/playlist/457PRAhJMUXaS8s6Evh6Hd?si=1ed9174c5d254d54"
elif cname == "yellow":
    playlist_id = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO3CRVnO?si=bfa09e761860439f"

print(playlist_id)

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



