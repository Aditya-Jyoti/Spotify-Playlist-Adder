import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os

class PlaylistInteractor:
    def __init__(self, song):
        # with open('secrets.json', 'r') as f:
        #     content = json.load(f)

        self.SPOTIFY = spotipy.Spotify(
            auth_manager= SpotifyOAuth(
                client_id= os.environ["spotify_client_id"],
                client_secret= os.environ["spotify_client_secret"],
                redirect_uri= "http://localhost:8888/callback/",
                scope="playlist-modify-public"                
            )
        )
        self.PLAYLIST_ID = "2jI2CmTU2XTIPqQl7gXn4K"
        self.song = song 
        
    def addToPlaylist(self):
        self.SPOTIFY.playlist_add_items(
            self.PLAYLIST_ID, self.song
        ) 
        
if __name__ == "__main__":
    interactor = PlaylistInteractor(["75ls0gurX68lUmMjE7QcsE"])
    interactor.addToPlaylist()        
        
