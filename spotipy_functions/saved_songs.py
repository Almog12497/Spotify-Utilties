import spotipy
import create_auth
from spotipy.oauth2 import SpotifyOAuth

class Favorite:
    scope = "user-top-read,user-library-read,playlist-modify-public,user-read-recently-played,playlist-read-private,user-read-currently-playing,playlist-modify-public"
    sp = create_auth.auth(scope)
    _list = []

    def __init__(self):
        pass

    def show_tracks(self,results):
        for item in results['items']:
            track = item['track']
            print((track['artists'][0]['name'], track['name']))

    def show_tracks_id(self,results):
        for item in results['items']:
            track = item['track']
            self._list.append(track['id'])
            print((track['id']))
    
    def show_all_ids(self):
        self._list = []
        results = self.sp.current_user_saved_tracks()
        self.show_tracks_id(results)
        while results['next']:
            results = self.sp.next(results)
            self.show_tracks_id(results)
        return self._list

    def show_all(self):
        self._list = []
        results = self.sp.current_user_saved_tracks()
        self.show_tracks(results)
        while results['next']:
            results = self.sp.next(results)
            self.show_tracks(results)
        return self._list





if __name__ == '__main__':
    a = Favorite()
    a.show_all()