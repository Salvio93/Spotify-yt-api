import requests,sys
SPOTIFY_GET_PLAYLIST_ITEM = "https://api.spotify.com/v1/playlists/5Xzb6hPh8wERGRh2MVK4Ee/tracks"

ACCESS_TOKEN = "BQDSBdtgaO7_EWjqdIWB3nYNVD3iHAIlPYWGdPCpf28eupwrghqsgzAaiQfSlesRrFvE30_Ovj3qbmvbIUABpB9C19IOLbTk0jXqH7BBqdFrOaxdyL0IZnbEc95qNaktBUsyOfD0FoUeiHYOnH62tDIUhVIkt7e6ijNj47rJZc2lOlx2xqF_ntwHl9y81BjEG68nM5RrfrteTpe6lUU"
artist = {}
playname = "5Xzb6hPh8wERGRh2MVK4Ee"
#fct to get a numb of item from a spotify playlist
def get_playlist_item(natio,limit):
    response = requests.get(
        SPOTIFY_GET_PLAYLIST_ITEM,
        headers={
            "Authorization" : f"Bearer {ACCESS_TOKEN}"
        }
        
    )
    json_rep = response.json()

    
    for e in range(limit):
        artist[str(json_rep['items'][e]['track']['album']['artists'][0]['name']) ] = str(json_rep['items'][e]['track']['name'])
    

    return artist

    

def main(natio = "BE", limit = 15):
    playlist_item = get_playlist_item(
        natio , limit)
    
    sys.stdout = open('spotify_list','w')
    print(f"Playlist_item: {playlist_item} \n")

    for e in range(limit):
        print(playlist_item.items(e))
        print("\n")
    sys.stdout.close()


    