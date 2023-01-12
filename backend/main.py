from fastapi import FastAPI, HTTPException
from models import Track, Playlist
import json

app = FastAPI()

# json files database
# Load the tracks from the JSON file
with open("./db/tracks.json", "r") as f:
    tracks = json.load(f)

# Load the playlists from the JSON file
with open("./db/playlists.json", "r") as f:
    playlists = json.load(f)

# Read a specific track
@app.get("/tracks/{track_id}")
def read_track(track_id: int):
    for track in tracks:
        if track['id'] == track_id:
            return Track(**track)
    raise HTTPException(status_code=404, detail="Track not found")

# Create a new track
@app.post("/tracks")
def create_track(track: Track):
    if any(x['id'] == track.id for x in tracks):
        raise HTTPException(status_code=409, detail="Track already exists")
    tracks.append(track.dict())
    return track

# Delete a specific track
@app.delete("/tracks/{track_id}")
def delete_track(track_id: int):
    global tracks, playlists
    tracks = [track for track in tracks if track['id'] != track_id]
    for playlist in playlists:
        if track_id in playlist['tracks']:
            playlist['tracks'].remove(track_id)
    return {"message": "Track deleted"}
# @app.delete("/tracks/{track_id}")
# def delete_track(track_id: int):
#     global tracks
#     tracks = [track for track in tracks if track['id'] != track_id]
#     return {"message": "Track deleted"}

# Create a new playlist
@app.post("/playlists")
def create_playlist(playlist: Playlist):
    if any(x['id'] == playlist.id for x in playlists):
        raise HTTPException(status_code=409, detail="Playlist already exists")
    playlists.append(playlist.dict())
    return playlist

# Read a specific playlist
@app.get("/playlists/{playlist_id}")
def read_playlist(playlist_id: int):
    for playlist in playlists:
        if playlist['id'] == playlist_id:
            return Playlist(**playlist)
    raise HTTPException(status_code=404, detail="Playlist not found")

# Delete a specific playlist
@app.delete("/playlists/{playlist_id}")
def delete_playlist(playlist_id: int):
    global playlists
    playlists = [
        playlist for playlist in playlists if playlist['id'] != playlist_id]
    return {"message": "Playlist deleted"}
