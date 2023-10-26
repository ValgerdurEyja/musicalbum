#from typing import Any


class MusicAlbum:
    def __init__(self, band = "unknown band", title = "unknown", year = "unknown year") -> None:
        self.band = band
        self.title = title
        self.year = year
    
    def set_album(self, band = None, title = None, year = None):
        if band != None:
            self.band = band
        if title != None:
            self.title = title
        if year != None:
            self.year = year
    def __str__(self) -> str:
        return f"{self.band}, released {self.title} in {self.year}."