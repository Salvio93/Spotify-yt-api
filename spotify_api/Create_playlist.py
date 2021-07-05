import requests

SPOTIFY_CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/salvio6140/playlists"
ACCESS_TOKEN = "BQA69hlQ1YBVMBQiECcDk3oAdbExW_3n_r3K50aaWLmqAi2Fp-suLg1Z3D9xcv_Cxqg53pe_ucuLbZPwn0lbKzLIBoXqT6uaNGiuPoXsNU1KsJ49PALi9FhtGpso2BBdIQCOkOqF6VSKEaBstAuD3nfDUumu3SvGtPnlhawnj1huEu0EXmcT2SXL08LMKleIbiRpHucc"

def create_playlist(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization" : f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name" : name,
            "public" : public
        }
    )
    json_rep = response.json()

    return json_rep
    

def main():
    playlist = create_playlist(
        name ="api Playlist",
        public = True
    )
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()