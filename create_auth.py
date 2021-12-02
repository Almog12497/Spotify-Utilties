import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def auth(_scope="user-top-read"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.secrets.client_id(),
                                               client_secret=secrets.secrets.client_secret(),
                                               redirect_uri=secrets.secrets.redirect_url(),
                                               scope=_scope))
    return sp
    
