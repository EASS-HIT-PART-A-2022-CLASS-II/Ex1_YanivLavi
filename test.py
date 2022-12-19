import requests
# from models import *
# from main import *

# Create a new track
track_data = {
    "id": 1,
    "name": "Sweet Child o' Mine",
    "artist": "Guns N' Roses",
    "album": "Appetite for Destruction",
    "genre": "Rock",
    "duration": "180"
}

# Create a new playlist
playlist_data = {
    "id": 1,
    "name": "My Favorite Songs",
    "tracks": [track_data]
}

r = requests.post("http://localhost:8989/tracks", json=track_data)
print("added track:")
print(r.json())

r = requests.post("http://localhost:8989/playlists", json=playlist_data)
print("\nCreated a playlist and added the track:")
print(r.json())

# Read the track
r = requests.get("http://localhost:8989/tracks/1")
print("\nReading track info:")
print(r.json())

# Read the playlist
r = requests.get("http://localhost:8989/playlists/1")
print("\nReading playlist info:")
print(r.json())

# # Delete the track
# r = requests.delete("http://localhost:8989/tracks/1")
# print(r.json())
