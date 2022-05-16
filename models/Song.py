from pydantic import BaseModel


class Song(BaseModel):
    avatar: str
    bgImage: str
    coverImage: str
    creator: str
    lyric: str
    music: str
    title: str
    url: str
