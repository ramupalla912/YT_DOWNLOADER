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
