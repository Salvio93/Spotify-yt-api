from pytube import YouTube
import Search_yt_api, Get_playlist_item
import os

  
#link of the video to be downloaded 
links = Search_yt_api.ending()
print(links)
# url input from user
for e in links:
    if e != None:
        yt = YouTube(e)
        # extract only audio
        video = yt.streams.filter(only_audio=True).first()
        
        # check for destination to save file
        destination = "~/Bureau/spotify_api" 
        
        # download the file
        out_file = video.download(output_path=destination)
        
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
  
