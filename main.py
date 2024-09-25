from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import yt_dlp
import os

app = FastAPI()

# CORS Middleware to allow all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; specify the required origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/yt")
async def download_video(url: str = Form(...)):
    # Get the user's default download folder path
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # yt-dlp options to download to the user's download folder
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output file in default download folder
    }

    try:
        # Using yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        return {"status": "Downloaded Successfully!", "path": download_path}
    except Exception as e:
        return {"status": f"Failed to download video: {str(e)}"}

    
#------------------------------------

# @app.post("/download/")
# async def download_video(url: str = Form(...)):
#     ydl_opts = {
#         'format': 'best',
#         'outtmpl': '%(title)s.%(ext)s',  # Output file name
#         # 'outtmpl': os.path.join(cur_dir, "required_name.mp4")
#     }
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         # Sending acknowledgment to the frontend
#         return {"status": "Downloaded Successfully!"}
#     except Exception as e:
#         # If there's an error, send a failure response
#         return {"status": f"Failed to download video: {str(e)}"}



# # Provide the YouTube video URL
# video_url = "https://youtu.be/LCI2OZiV5UQ?si=pD_1NrcDp2kVIGN1"
# download_video(video_url)



# import yt_dlp
# import os

# def download_video(url, download_path):
#     # Create the download path if it doesn't exist
#     if not os.path.exists(download_path):
#         os.makedirs(download_path)

#     ydl_opts = {
#         'format': 'bestvideo+bestaudio/best',  # Best video + best audio, or best overall
#         'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Output file name with path
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])

# # Provide the YouTube video URL
# video_url = "https://youtu.be/LCI2OZiV5UQ?si=pD_1NrcDp2kVIGN1"
# # Specify the download path
# download_path = "D:/yt_main_downloads"  # Change this to your desired path
# download_video(video_url, download_path)
