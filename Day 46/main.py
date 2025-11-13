import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "1723c9f90c4041b8ac302aac513a6645"
CLIENT_SECRET = "7306ff7040434f07bbb2b8e59d81b06f"
REDIRECT_URI = "http://127.0.0.1:8888/callback"  # ✅ Use IP instead of localhost

scope = "user-library-read playlist-modify-public playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=scope
))


#
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
          "Accept-Language": "en-US,en;q=0.9",
          }

year_wanted_to_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
URL = f"https://www.billboard.com/charts/hot-100/{year_wanted_to_travel}/"
response = requests.get(URL,headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")


# Check your profile info to confirm authentication
def check_spotify_authentication():
    print("Testing Spotify API connection...")
    user_profile = sp.current_user()
    print(f"Logged in as: {user_profile['display_name']} ({user_profile['id']})")


#display date from the Billboard page
def display_web_chart_date():
    # --- Find all spans with class 'c-span'
    all_spans = soup.find_all("span", class_="c-span")
    # The chart date is usually the one that starts with 'Week of'
    song_hit_date = None
    for span in all_spans:
        text = span.get_text(strip=True)
        if text.startswith("Week of"):
            song_hit_date = text
            break

    if song_hit_date:
        return print(f"Billboard Hot 100 - {song_hit_date}\n")
    else:
        return print("Chart date not found!")



#scraping in the Billboard web music lists
song_hit_titles = soup.select("li h3.c-title")
song_hit_titles_lists =[song.get_text(strip=True) for song in song_hit_titles]

display_web_chart_date()
print(song_hit_titles_lists)

check_spotify_authentication()

# Search Billboard top hits on Spotify and collect URIs
track_uris = []
for song in song_hit_titles_lists:
    result = sp.search(q=song, limit=1, type="track")
    tracks = result["tracks"]["items"]

    if tracks:
        uri = tracks[0]["uri"]
        track_uris.append(uri)
        print(f"Found: {song} → {tracks[0]['external_urls']['spotify']}")
    else:
        print(f"Not found on Spotify: {song}")

print(f"\nTotal songs found on Spotify: {len(track_uris)}")


user_id = sp.current_user()["id"]

# Create a playlist named after the Billboard chart date
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Hot 100 - {year_wanted_to_travel}",
    public=True
)

# Add the songs we found
sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
print(f"\nPlaylist created: {playlist['external_urls']['spotify']}")



