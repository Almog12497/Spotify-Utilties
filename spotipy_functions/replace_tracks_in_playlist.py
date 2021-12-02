import spotipy
import create_auth
import pprint
import sys
from spotipy.oauth2 import SpotifyOAuth

track_ids = ['328RAUNA3SYuWxg4OClYGq', '7apcnerZJaEWx3zJNLhWGt', '667eE4CFfNtJloC6Lvmgrx', '6MvVIgWOfAqU9rGAt94DQ5', '5IdRCNAdlvR7bSoXkmB12m', '37s8uwIjw72XfMseKJXNOO', '0HUGL7rKvVtVV0VhFqGMZO', '68wEEgRMaFv0PXYVgCQrtp', '2uTqluJ3zGMpyiNQr8skml', '1FBINzSbI9W6jKdzChRQSp', '42ggMOYB5MYmP6RN4SZwWt', '5O7KOryUNhEK5ev7OLWUGe', '5ZBs9dRavxKAS23WT1MwkQ', '1AMzUKhF0vCFHZTx8H7OS4', '2xv88nEtQu8cGKzBFWqzF0', '1HlumBvclGhCA2PwRlrFP5', '7LD7MAqY0E3BzPnUwrWfIv', '6bHaS4HXtOSh5yUinofdzu', '5nZ9E3ZCdwj6VYnFgF6yHF', '7xHrqNdRTjVmvualewApyl', '1ZjvIaEJRjamDwcypUGbpr', '1359Fb2E2YOo7D8pVKWpwV', '0CALOqrkXAE7WB2nyIATLk', '6IsLwvMwI1c7CdY2xuBAtM', '3FzYpRX5BO5xGLFWuICD4p', '0tjGbehnu4hSi7S5j1GuuR', '2oGfxSUjuytuPLj1Xn1NxV', '1M5oAZm8pkNtArxy9zUxsQ', '4skaXyEuciTFITCNwYW6wH', '4yNHnUvkGrjuHlIg1lQ7JP', '3HyjVZQoE51NojVIfDWJbx', '7evqymsKRg36lAeakXrNcS', '2aozlm4HfRx8yRYL7RCoAH', '22a306esXR3a9CdrBQcRr8', '0wHNzLTeVSOF7iAH4C8Kv9', '6sI0EWeLu1Gi2fqShtyXDP', '6y1jU3MtV2vdVfm5y7f9uo', '36482hNESSwELpr9sS3NbE', '0wjRgnKbm1OKk3sMKgYf17', '2xeiJGUGH7NbJ0BOh7Q6QT', '5G0qIOnEN61RcOPeiBJ4se', '2HZDTwJgohQGpqNR5CIrd7', '4ZnzACAqoHD88be6zCX1Z8', '2r6wHo822G5gpVa7IXXoMu', '2iGt8kJKM7cUF9TEr50XGF', '6pb74p1J3mKnEEf7J1X8VO', '5DYNsmAZ7Tfgj8G2LQGdr1', '4dCecGxHxWnDG62FHrtogw', '2bkKIbuGeTw2jktv3oGMAR', '0adpMk52noKN7rxBQIWLJ4']
sp = create_auth.auth("playlist-modify-public")
def replace(playlist_id,track_ids):
  length = len(track_ids)
  if length > 100 :
    iterations = int(length / 100)
    for i in range(iterations+1):
      i += 1
      upper_limit= i*100
      lower_limit = upper_limit - 100
      sp.playlist_replace_items(playlist_id, track_ids[lower_limit:upper_limit])
  else:
         sp.playlist_replace_items(playlist_id, track_ids)
 


def add(playlist_id,track_ids):
  length = len(track_ids)
  if length > 100 :
    iterations = int(length / 100)
  for i in range(iterations+1):
    i += 1
    upper_limit= i*100
    lower_limit = upper_limit - 100
    sp.playlist_add_items(playlist_id, track_ids[lower_limit:upper_limit])
