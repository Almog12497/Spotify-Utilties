from logging import raiseExceptions
import create_auth
import spotipy
from collections import Counter

from spotipy_functions import *
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

print(top_playlists)

