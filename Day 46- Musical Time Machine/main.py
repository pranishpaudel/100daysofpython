###SCRAP DATA FROM WEBSITE###
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth



CLIENT_ID= "958e0602fc4e4549b875d5b9518a7c2b"
CLIENT_SECRET= "40aaa75a1b7740a9a893dd28adee7552"
REDIRECT_URI = 'http://localhost:8000/callback'

User_demand_date= "2008-11-15"

ENDPOINT_URL= f"https://www.billboard.com/charts/hot-100/{User_demand_date}/"

html_data= requests.get(ENDPOINT_URL).text

soup= BeautifulSoup(html_data,"html.parser")

song_names_spans = soup.select("li ul li h3")

song_names = [song.text.strip() for song in song_names_spans]
print(song_names)

#####CREATE THE PLAYLIST######
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='playlist-modify-private'))  # or 'playlist-modify-public' if desired

# current_play = sp.current_user_playlists()
# print(current_play)
def create_playlist(name, is_public=False):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=name, public=is_public)
    return playlist['id']

playlist_name = f"song {User_demand_date}"
is_public = False

    # Create the playlist
playlist_id = create_playlist(playlist_name, is_public)
print(playlist_id)

def search_and_get_track_uri(track_name):
    results = sp.search(q=track_name, type='track', limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['uri']
    else:
        return None

# Function to add a track to a playlist
def add_track_to_playlist(playlist_id, track_uri):
    sp.playlist_add_items(playlist_id, [track_uri])

for add_song in song_names:
    # Specify the playlist ID and the track name
    track_name = add_song  # Replace with the desired song name

        # Search for the track by name
    track_uri = search_and_get_track_uri(track_name)
    print(track_uri)

    if track_uri:
            # Add the track to the playlist
            add_track_to_playlist(playlist_id, track_uri)
            print(f"The track '{track_name}' has been added to the playlist.")
    else:
            print(f"No track found with the name '{track_name}'.")
# for song in song_names_spans:

#     song_file= open("Day 46- Musical Time Machine/song.txt","a")
#     song_file.write(song.text.strip()+"\n")
