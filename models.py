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
    genre: str = ""
    duration: int = 1
    # owner: User

    # def add_to_playlist(self, playlist: Playlist):
    #     playlist.add_track(self)

    # def remove_from_playlist(self, playlist: Playlist):
    #     playlist.remove_track(self)

    def get_info(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'duration': self.duration,
            'genre': self.genre
        }


class Playlist(BaseModel):
    id: int
    name: str
    tracks: List[Track]
    # owner: User

    def add_track(self, track: Track):
        self.tracks.append(track)

    def remove_track(self, track: Track):
        self.tracks.remove(track)


