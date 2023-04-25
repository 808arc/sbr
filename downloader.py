# importing packages
import os
import time
from pytube import YouTube

def get_link_loader (link_list):
    destination = 'Tracks'

    for link in link_list:
        try:
            # url input from user
            yt = YouTube(str(link))

            # get the audio stream
            video = yt.streams.filter(only_audio=True).first()

            # download the file
            out_file = video.download(output_path=destination)

            # save the file as an MP3
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            # result of success
            print(yt.title + " has been successfully downloaded.")
            time.sleep(10)

        except Exception as e:
            # handle errors
            print(f"Error downloading video {link}: {e}")
