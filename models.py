
from pydantic import BaseModel
import json

class User(BaseModel):
    id: int
    username: str

class Track(BaseModel):
    id: int = 0
    name: str = "asdasd"
    artist: str = "asdsad"
    type: str = "mp3"
    length: str = "3:14"
    size: str = "12155KB"
    created: str = "12/12/2013"
    owner: User = {"0","user1"}
    path: str = "/user/home/track01.mp3"

class Playlist(BaseModel):
    user: User
    tracks: list

def add_track_to_playlist(Track):
    # get list of tracks by user
    #tracks.insert(Track)
    return Track

def add_track(Track):
    # add track todo
    return Track

def delete_track(Track):
    #del track todo
    return Track

# def track_info(id):
#     #todo 
#     return id

