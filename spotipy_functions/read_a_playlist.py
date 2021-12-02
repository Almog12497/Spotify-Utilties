import spotipy

class Read_Playlist():
    def __init__ (self,sp,user,playlist_id):
        self.sp = sp
        self.user = user
        self.playlist_id = playlist_id

    def read(self):
        results = self.sp.playlist(self.playlist_id)
        print(results)


# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print(
#             "%4d %s %s" %
#             (i +
#              1 +
#              playlists['offset'],
#              playlist['uri'],
#              playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None