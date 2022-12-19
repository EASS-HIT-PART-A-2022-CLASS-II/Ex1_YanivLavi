import requests

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
    "tracks": [track_data, track_data, track_data]
}

print("Testing...")
print("Creating a track and a playlist, add the track 3 times to the playlist, read track, read playlist")

print(
    "\nPossible response codes:\n200: json is returned\n404: Not found\n409: Already exists\n\n")

r = requests.post("http://localhost:8989/tracks", json=track_data)
print("Trying to create a track using post request to http://localhost:8989/tracks")
print("Request: ")
print(track_data)
print("Response: ")
print(str(r.status_code))
print(r.json())

r = requests.post("http://localhost:8989/playlists", json=playlist_data)
print("\nTrying to create a playlist using post request to http://localhost:8989/playlists")
print("Request: ")
print(playlist_data)
print("Response: ")
print(str(r.status_code))
print(r.json())

# Read the track
r = requests.get("http://localhost:8989/tracks/1")
print("\nReading track info from http://localhost:8989/tracks/1:")
print(r.json())

# Read the playlist
r = requests.get("http://localhost:8989/playlists/1")
print("\nReading playlist info from http://localhost:8989/playlists/1:")
print(r.json())

# # Delete the track
# r = requests.delete("http://localhost:8989/tracks/1")
# print(r.json())