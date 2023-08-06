import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_client_id',
                                               client_secret='your_client_secret',
                                               redirect_uri='your_redirect_uri',
                                               scope='your_required_scopes'))

# Get current user
user_id = sp.current_user()["id"]

# Ask user to input a date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# The list of song names
song_names = ["The list of song", "titles from your", "web scrape"]

# Empty list to store song URIs
song_uris = []

# Search songs by name and year, and retrieve their URIs
for song in song_names:
    try:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
