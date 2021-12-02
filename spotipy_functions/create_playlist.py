import spotipy
import create_auth
from spotipy.oauth2 import SpotifyOAuth

def create(_name,_description):
    scope = "playlist-modify-public"
    sp = create_auth.auth(scope)
    user_id = sp.me()['id']
    sp.user_playlist_create(user_id , name = _name,description=_description, public =True)

