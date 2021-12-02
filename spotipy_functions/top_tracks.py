import spotipy
import create_auth

list = []
sp = create_auth.auth("user-top-read")
def top_tracks (time_range,limit,offset):  
 results = sp.current_user_top_tracks(time_range=time_range, limit=limit,offset=offset)
 for i, item in enumerate(results['items']):
        print(i+offset, item['name'], '//', item['artists'][0]['name'])


def top_tracks_ids (time_range,limit,offset): 
   results = sp.current_user_top_tracks(time_range=time_range, limit=limit,offset=offset)
   for i, item in enumerate(results['items']):
      list.append(item['id'])
   return list







