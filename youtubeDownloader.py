from pytube import YouTube # type: ignore
from pytube.cli import on_progress # type: ignore
from datetime import timedelta

# Insert download path
SAVE_PATH = 'G:/Personal/Peliculas' 

link=input('\nInsert Youtube url: ')

# Create a yt object with progressbar and link
yt=YouTube(link,on_progress_callback=on_progress)

# File_extension
videos = yt.streams.filter(file_extension='mp4', progressive=True)

# Best possible quality
d_video = videos[-1]

# Video length formatted
duration = yt.length
duration_formatted = str(timedelta(seconds=duration))

print(f"\n[+] Video Title: \"\033[1m{yt.title}\033[0m\" \n[+] Youtube Channel Name: \033[1m{yt.author}\033[0m \n[+] Youtube Channel Url: \033[1m{yt.channel_url}\033[0m \n[+] Video Length: \033[1m{duration_formatted}\033[0m  \n[+] Publish Date: \033[1m{yt.publish_date}\033[0m\n")

# Download video
d_video.download(output_path=SAVE_PATH)

print(f"\n\n✅ Youtube Video \"\033[1m{yt.title}\033[0m\" downloaded successfully")
