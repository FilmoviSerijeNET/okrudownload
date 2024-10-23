import yt_dlp

def download_ok_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'outtmpl': '%(title)s.%(ext)s',  
        'merge_output_format': 'mp4',  
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Ok.ru link: ")
    download_ok_video(video_url)
    print("Preuzimanje završeno!")
