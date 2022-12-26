from pydantic import BaseModel
import json
from typing import List


class User(BaseModel):
    id: int
    name: str
    email: str

class Track(BaseModel):
    id: int
    name: str
    artist: str
    album: str
    genre: str 
    duration: int 
    # owner: User

    def get_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist,
            'album': self.album,
            'genre': self.genre,
            'duration': self.duration
            
        }
# ,'owner': self.owner

class Playlist(BaseModel):
    id: int
    name: str
    tracks: List[Track]
    # owner: User

    def add_track(self, track: Track):
        self.tracks.append(track)

    def remove_track(self, track: Track):
        self.tracks.remove(track)


