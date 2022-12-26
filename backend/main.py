from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from typing import List
from models import *

app = FastAPI()

# In-memory database 
users = {}
tracks = {}
playlists = {}

# Read a specific track
@app.get("/tracks/{track_id}")
def read_track(track_id: int):
    if track_id not in tracks:
        raise HTTPException(status_code=404, detail="Track not found")
    track = tracks[track_id]
    return {"id": track.id, "name": track.name, "artist": track.artist, "album": track.album, "genre": track.genre, "duration": track.duration}
    # return {track.get_info()}

# Create a new track
@app.post("/tracks")
def create_track(track: Track):
    if track.id in tracks:
        raise HTTPException(status_code=409, detail="Track already exists")
    tracks[track.id] = track
    return {"id": track.id, "name": track.name, "artist": track.artist, "album": track.album, "genre": track.genre, "duration": track.duration}

# Delete a specific track
@app.delete("/tracks/{track_id}")
def delete_track(track_id: int):
    if track_id not in tracks:
        raise HTTPException(status_code=404, detail="Track not found")
    del tracks[track_id]
    return {"message": "Track deleted"}

    
# Create a new playlist
@app.post("/playlists")
def create_playlist(playlist: Playlist):
    if playlist.id in playlists:
        raise HTTPException(status_code=409, detail="Playlist already exists")
    playlists[playlist.id] = playlist
    return {"id": playlist.id, "name": playlist.name, "tracks": playlist.tracks}

# Read a specific playlist
@app.get("/playlists/{playlist_id}")
def read_playlist(playlist_id: int):
    if playlist_id not in playlists:
        raise HTTPException(status_code=404, detail="Playlist not found")
    playlist = playlists[playlist_id]
    return {"id": playlist.id, "name": playlist.name, "tracks": playlist.tracks}

# Delete a specific playlist
@app.delete("/playlists/{playlist_id}")
def delete_playlist(playlist_id: int):
    if playlist_id not in playlists:
        raise HTTPException(status_code=404, detail="Playlist not found")
    del playlists[playlist_id]
    return {"message": "Playlist deleted"}

# #user endpoints
# @app.post("/users")
# def create_user(user: User):
#     # Save the user to the database
#     save_user(user)
#     return {"id": user.id, "name": user.name, "email": user.email}

# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     # Get the user from the database
#     user = get_user_by_id(user_id)
#     if user:
#         return {"id": user.id, "name": user.name, "email": user.email}
#     else:
#         return {"error": "User not found"}

# @app.put("/users/{user_id}")
# def update_user(user_id: int, user: User):
#     # Get the user from the database
#     user = get_user_by_id(user_id)
#     if user:
#         # Update the user and save it to the database
#         user.name = user.name
#         user.email = user.email
#         save_user(user)
#         return {"id": user.id, "name": user.name, "email": user.email}
#     else:
#         return {"error": "User not found"}

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int):
#     # Get the user from the database
#     user = get_user_by_id(user_id)
#     if user:
#         # Delete the user from the database
#         delete_user(user)
#         return {"message": "User deleted"}
#     else:
#         return {"error": "User not found"}

