from pytube import YouTube
from pytube.cli import on_progress
from datetime import timedelta
import tkinter as tk
from tkinter import filedialog
import os
from platformdirs import user_downloads_dir

yt = ""


def checkLink(link):
    error = True
    try:
        yt = YouTube(link,on_progress_callback=on_progress)
        error = False
    except UnboundLocalError as e:
        print(e)
    finally:
        if (error):
            return ""
        else:
            return yt

def select_path():
    tk.Tk()
    path = filedialog.askdirectory()
    return path

link = input('\n[#] Insert Youtube url: ')

path = user_downloads_dir()

yt = checkLink(link)

if (yt != ""):

    # File_extension
    videos = yt.streams.filter(file_extension='mp4', progressive=True)

    # Best possible quality
    d_video = videos[-1]

    # Video length formatted
    duration = yt.length
    duration_formatted = str(timedelta(seconds=duration))

    print(f"\n[+] Video Title: \"\033[1m{yt.title}\033[0m\" \n[+] Youtube Channel Name: \033[1m{yt.author}\033[0m \n[+] Youtube Channel Url: \033[1m{yt.channel_url}\033[0m \n[+] Video Length: \033[1m{duration_formatted}\033[0m  \n[+] Publish Date: \033[1m{yt.publish_date}\033[0m\n")

    # Download video
    d_video.download(output_path=path)

    print(f"\n\n✅ Youtube Video \"\033[1m{yt.title}\033[0m\" downloaded successfully")

else:
    print("\n[!] The video link is wrong")