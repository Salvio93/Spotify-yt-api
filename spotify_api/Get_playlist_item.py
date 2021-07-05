import requests,sys
SPOTIFY_GET_PLAYLIST_ITEM = "https://api.spotify.com/v1/playlists/5Xzb6hPh8wERGRh2MVK4Ee/tracks"
ACCESS_TOKEN = "BQAX4NXWi5VNQ-eYQOU53PrdVcHAcQDGZLK61I21T6AuQ-FIThKs5rZkPslMxuD_dAj5lXTyQabLbVlR_zmZpL4BhJ52kNCvQWqQUtKVaHcuT1RQYeMOREwJgnwk0XoVHM2m2Q8kEx5LphdWp1efxWQ33qWr_EpyjJjHcDDFgoqp93EnNbx1u1eI3P5MgYEfD-g1kBryeFlQ0oKE5Q8"
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
    print(f"Playlist_item: {playlist_item}")
    sys.stdout.close()


    