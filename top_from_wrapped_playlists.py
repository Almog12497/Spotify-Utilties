from logging import raiseExceptions
import create_auth
import spotipy
from collections import Counter
from pprint import pprint

from spotipy_functions import *
from spotipy_functions import read_a_playlist
from spotipy_functions.read_playlists import Playlist

#Scopes we need to access
sp = create_auth.auth("user-top-read,user-library-read,playlist-modify-public,user-read-recently-played,playlist-read-private,user-read-currently-playing,playlist-modify-public")
playlists = read_playlists.Playlist(sp)

playlists_ids = playlists.show_playlists_ids()
playlists_names =playlists.show_playlists()

top_playlists = []

for i,name in enumerate(playlists_names):
    if "Your Top Songs" in name:
        top_playlists.append((name,playlists_ids[i]))

all_songs = []

for playlist_id in top_playlists:
    temp_playlist = playlist_id[1]
    temp_playlist = read_a_playlist.Read_Playlist(sp,"almog12497",temp_playlist)
    all_songs.append(temp_playlist.read())

count_artists = []

for playlist in all_songs:
    temp = []
    for artist in playlist:
        artist = artist[2]
        temp.append(artist)
    count_artists.append(Counter(temp))

for i,playlist in enumerate(count_artists):
    pprint(f"Top Artists in {top_playlists[i][0]} : ")
    pprint(count_artists[i])

count_songs = []

for playlist in all_songs:
    temp = []
    for song in playlist:
        song = (song[1],song[2])
        temp.append(song)
    count_songs.extend(temp)
count_songs = Counter(count_songs)
print("Songs that appeared multiple years in a row:")
appear_multiple_times = {k:v for k,v in count_songs.items() if v > 1}
appear_multiple_times = (sorted(appear_multiple_times,key = lambda item:item[1]))
pprint(appear_multiple_times)