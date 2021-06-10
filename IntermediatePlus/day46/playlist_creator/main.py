import requests
from bs4 import BeautifulSoup
import datetime as dt
import spotipy
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

scope = "playlist-modify-public"

sp = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                 client_secret=SPOTIFY_CLIENT_SECRET,
                                 redirect_uri=SPOTIFY_REDIRECT_URI,
                                 scope=scope,
                                 cache_path="token.txt",
                                 requests_session=True)

spotify = spotipy.client.Spotify(oauth_manager=sp)

user = spotify.current_user()
username = user['display_name']
user_id = user['id']
print(f"{username}: {user_id}")


def get_date():
    valid = False
    while not valid:
        date = input("Enter a date in 'YYYY-MM-DD' format: ")
        year = int(date.split("-")[0])
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])
        try:
            valid_date = dt.date(year, month, day)
            valid = True
        except ValueError:
            print("\nPlease enter a valid date in the proper format.\n")

    date = valid_date.strftime("%Y-%m-%d")
    return date


search_date = get_date()

hot_hundred_res = requests.get(url=f"https://www.billboard.com/charts/hot-100/{search_date}")

soup = BeautifulSoup(hot_hundred_res.text, "html.parser")

artists_soup = soup.find_all(name="span", class_="chart-element__information__artist")
artists = [artist.get_text() for artist in artists_soup]

songs_soup = soup.find_all(name="span", class_="chart-element__information__song")
songs = [song.get_text() for song in songs_soup]

titles_artists = []
for i in range(len(artists)):
    titles_artists.append((songs[i], artists[i]))

not_found_list = []


def get_uri(title, artist):
    query = (title, artist)
    try:
        track_obj = spotify.search(q=query, limit=1, type='track')
        track_uri = track_obj['tracks']['items'][0]['uri']
    except IndexError:
        not_found_list.append((title, artist))
        return ''
    return track_uri


uri_list = []
for item in titles_artists:
    uri = get_uri(item[0], item[1])
    if uri != '':
        uri_list.append(uri)

if len(not_found_list) > 0:
    print(f"Songs not found: {not_found_list}")

playlist = spotify.user_playlist_create(user=user_id, name=f"{search_date} Billboard Hot 100", public=True)
playlist_id = playlist['id']

playlist_snapshot = spotify.playlist_add_items(playlist_id=playlist_id, items=uri_list)
