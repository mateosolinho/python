from pytube import YouTube
from pytube.cli import on_progress
from datetime import timedelta
import tkinter as tk
from tkinter import filedialog
from platformdirs import user_downloads_dir

yt = ""
path = ""
link = ""

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
    res = input("\n[?] Do you want to select a destination path? (y/n) ")
    match res:
        case "y":
            tk.Tk()
            path = filedialog.askdirectory()
            tk.Tk().withdraw()
        case "n":
            path = user_downloads_dir()
        case _:
            print("\n[!] Wrong format, using default download path") 
            path = user_downloads_dir()
    return path

link = input('\n[#] Insert Youtube url: ')

yt = checkLink(link)

path = select_path()

if (yt != ""):

    videos = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc()

    # Mirar de mejorar la calidad del video
    d_video = videos[-1]

    duration = yt.length
    duration_formatted = str(timedelta(seconds=duration))

    print(f"\n[+] Video Title: \"\033[1m{yt.title}\033[0m\"")
    print(f"[+] Youtube Channel Name: \033[1m{yt.author}\033[0m")
    print(f"[+] Youtube Channel Url: \033[1m{yt.channel_url}\033[0m")
    print(f"[+] Video Length: \033[1m{duration_formatted}\033[0m")
    print(f"[+] Publish Date: \033[1m{yt.publish_date}\033[0m")
    print(f"[+] Download Path: \033[1m{path}\033[0m")

    # Download video
    d_video.download(output_path=path)

    print(f"\n\n✅ Youtube Video \"\033[1m{yt.title}\033[0m\" downloaded successfully")

else:

    print("\n[!] The video link is wrong")