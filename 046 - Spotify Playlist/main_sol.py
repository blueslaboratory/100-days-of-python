# 19/07/2024
# Day - 046



##################################################
# DAY 46 PROJECT: SPOTIFY PLAYLIST

print("\n*** Welcome to the Spotify Time Machine! ***")

from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth



# STEP 1: Scraping

date = "2011-06-21"
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date, verify=False)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

for song in song_names:
    print(song)



# STEP 2: Authenticate

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='870c4fd08e78453ebaa4b5fe0637923f',
        client_secret='e3a4d99892954901bc1def95c4683697',
        show_dialog=True,
        cache_path=".\\046 - Spotify Playlist\\token_sol.txt",
        username='titiritest', 
    )
)

user_id = sp.current_user()["id"]



# STEP 3: Search for each song on spotify and add them to an uri list

song_uris = []
year = date.split("-")[0]

for song in song_names:
    
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        

        
# Step 4 - Creating and Adding to Spotify Playlist

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)