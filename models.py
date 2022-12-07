
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
    # owner: User = "asdasd"
    path: str = "/sdad/asddasd/sad.mp3"

def add_track(Track):
    # add track todo
    return Track

def delete_track(Track):
    #del track todo
    return Track

# def track_info(id):
#     #todo 
#     return id

