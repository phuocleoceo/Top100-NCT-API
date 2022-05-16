from typing import List, Optional
from pydantic import BaseModel


class Song(BaseModel):
    avatar: Optional[str] = ""
    bgImage: Optional[str] = ""
    coverImage: Optional[str] = ""
    creator: Optional[str] = ""
    lyric: Optional[str] = ""
    music: Optional[str] = ""
    title: Optional[str] = ""
    url: Optional[str] = ""


class Category(BaseModel):
    name: Optional[str] = ""
    url: Optional[str] = ""
    songs: Optional[List] = []
