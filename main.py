"""
The main code that will run the other parts.
"""
from logging import raiseExceptions
import create_auth
import spotipy

from spotipy_functions import *

#Scopes we need to access
sp = create_auth.auth("user-top-read,user-library-read,playlist-modify-public,user-read-recently-played,playlist-read-private,user-read-currently-playing,playlist-modify-public")

#Information of what the user can do
print ("long term, short term , long term or maybe liked songs?")

while True:
    range = input()
    if range == "short term" or range == "medium term" or range == "long term": #parse into the readable form
        range = range.split

        if len(range()) == 2: #in this case has to be one of the ranges
            range = range()[0] + '_' + range()[1]
            print (top_tracks.top_tracks(range,50,0))
            break
        else:
            print("Please type a logical word.")

    elif range == "liked songs":
        a = saved_songs.Favorite()
        a.show_all()
        break

print("Would you like to create a playlist from the following songs?[Yes,No]")
string = str.lower(input()) #change to lower case so we wont have to check capital options

while True:
    if string == 'yes' or string == 'no':
        if string == 'yes':
            if range == "short_term" or range == "medium_term" or range == "long_term":
                tracks_ids = top_tracks.top_tracks_ids(range,50,0) #reads the top tracks 
                id = read_playlists.Playlist.find_id(range) #reads the id of all the playlists and searches if the playlist exists
                if  id == None: #creates a playlist incase it doesnt exist
                    create_playlist.create(range,"An example")
                    id = read_playlists.Playlist.find_id(range)
                replace_tracks_in_playlist.replace(id,tracks_ids)
                print ("The playlist %s has been updated!" % (range))
                break
            elif range == "liked songs":
                tracks_ids = a.show_all_ids()
                id = read_playlists.Playlist.find_id(range)
                if id == None:
                    create_playlist.create(range,"An example")
                    id = read_playlists.Playlist.find_id(range)
                replace_tracks_in_playlist.replace(id,tracks_ids[0:100])               
                replace_tracks_in_playlist.add(id,tracks_ids[100:])
                print ("The playlist %s has been updated!" % (range))
                break
            else:
                raiseExceptions("error")

    else:
        print ("Please type either yes or no")
        string = input()
