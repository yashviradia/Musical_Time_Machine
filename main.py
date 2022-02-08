import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv(find_dotenv())

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD \n")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{user_date}"

# Authentication in Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

response = requests.get(BILLBOARD_URL)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

song_titles = soup.select(selector="li h3", id="title-of-a-story")
selected_list = []

for title in song_titles:
    selected_list.append(title.getText().split("\n")[1])

list_of_songs = selected_list[0:100]

# Searching Spotify for songs by title
song_uris = []
year = user_date.split("-")[0]
for song in list_of_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)