# 19/07/2024
# Day - 046



##################################################
# DAY 46 PROJECT: SPOTIFY PLAYLIST

print("\n*** Welcome to the Spotify Time Machine! ***")

from bs4 import BeautifulSoup
import requests

from spotipy.oauth2 import SpotifyOAuth
import spotipy 
# pip install spotipy

import pprint



# STEP 1: Scraping

date = "2011-06-21"
# date = input("Which year would you like to travel to in YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"
print(URL)

response = requests.get(URL, verify=False)
# print(response.text)

# This line of code does our parsing  
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select(selector="li ul li h3")

# For loop
for i in range(len(songs)-1):
    song_name = songs[i].getText().strip()
    print(song_name)

# List comprehension
songs_list = [song.getText().strip() for song in songs]



# STEP 2: Authenticate 

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = '870c4fd08e78453ebaa4b5fe0637923f',
    client_secret = 'e3a4d99892954901bc1def95c4683697',
    redirect_uri = 'http://example.com',
    scope = 'playlist-modify-private'
))

user_id = sp.current_user()["id"]



# STEP 3: Search for each song on spotify and add them to an uri list

year = date.split("-")[0]

# result = sp.search(
#     q = f"track: {songs_list[0]}, year: {year}",
#     limit = 1,
#     type = "track"
# )
        
# pprint.pp(result["tracks"]["items"][0]["uri"])

uri_list = []

for song in songs_list:
    
    result = sp.search(
        q = f"track: {song}, year: {year}",
        limit = 1,
        type = "track"
    )
    
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
        
    except:
        print(songs_list.index(song), "- URI wasn't appended")
        
    
# for uri in uri_list: print(uri)



# Step 4 - Creating and Adding to Spotify Playlist

playlist = sp.user_playlist_create(
    user = user_id,
    name = f"{date} Billboard 100",
    public = False,
    collaborative = False,
    description = "Day 46: Project"
)


sp.user_playlist_add_tracks(
    user = "titiritest",
    playlist_id = playlist["id"],
    tracks = uri_list
)