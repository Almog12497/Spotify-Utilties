import spotipy
import create_auth

scope = 'playlist-read-private'
sp = create_auth.auth(scope)
class Playlist():
    def __init__(self,sp):
        self.sp = sp
    
    def show_playlists(self):
        results = self.sp.current_user_playlists()
        list = []
        for i, item in enumerate(results['items']):
            list.append("%s" % (item['name']))
        return list

    def show_playlists_ids(self):
        results = self.sp.current_user_playlists()
        list = []
        for i, item in enumerate(results['items']):
            list.append("%s" % (item['id']))
        return list

    @classmethod
    def find_id(self,playlist_name):
        names = self.show_playlists()
        if playlist_name in names:
            i = names.index(playlist_name)
            ids = self.show_playlists_ids
            return ids()[i]
        else:
            return None 


