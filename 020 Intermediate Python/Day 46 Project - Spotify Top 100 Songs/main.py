from bs4 import BeautifulSoup
import requests

date = "2019-10-31"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
musics = response.text
soup = BeautifulSoup(musics,"html.parser")
titles= soup.find_all(name="h3", class_="c-title", id="title-of-a-story")
# print(titles)
title_list=[]
for title in titles:
    x=title.getText()
    if ":" not in x:
        x= x.replace("\n\n\t\n\t\n\t\t\n\t\t\t\t\t","")
        x = x.replace("\t\t\n\t\n", "")
        title_list.append(x)
title_list=title_list[3:102:1]
#print(title_list)

id = id
secret = secret

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=id,
        client_secret=secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
