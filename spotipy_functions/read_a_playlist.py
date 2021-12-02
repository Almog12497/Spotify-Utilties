import spotipy


class Read_Playlist():
    def __init__ (self,sp,user,playlist_id):
        self.sp = sp
        self.user = user
        self.playlist_id = playlist_id

    def read(self):
        edited_results = []
        results = self.sp.playlist_items(self.playlist_id)
        # print (results["items"][0]['track']["name"])
        for i,item in enumerate(results["items"]):
            edited_results.append((i,item['track']['name'],item['track']['artists'][0]['name'],item["track"]["id"]))
        return edited_results


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