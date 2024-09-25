***Introducing YT_DOWNLOADER—my very first web application built with the power of the FAST API framework! Effortlessly download your favorite YouTube videos by simply pasting the URL, and let the magic happen.***

### Follow these steps to run this project in your system successfully...

Got it! I'll include the steps to run the project along with the `frontend.html` file.

### Steps to Run YT_DOWNLOADER (with Frontend)

1. **Clone the repository:**
   First, clone the YT_DOWNLOADER project from GitHub:
   ```bash
   git clone https://github.com/your-username/YT_DOWNLOADER.git
   ```
   Navigate to the project directory:
   ```bash
   cd YT_DOWNLOADER
   ```

2. **Install Python (if not already installed):**
   Make sure Python is installed on your system. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

3. **Create a Virtual Environment (optional but recommended):**
   It is recommended to create a virtual environment to isolate project dependencies:
   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install FastAPI and other dependencies:**
   Install FastAPI and `yt-dlp` by running the following commands:
   ```bash
   pip install fastapi
   pip install yt-dlp
   ```

5. **Run the FastAPI server:**
   You can start the FastAPI server using the following command:
   ```bash
   fastapi dev main.py
   ```

6. **Access the Frontend:**
   - After running the FastAPI server, open the `frontend.html` file in a web browser by navigating to the file path.
   - You can submit a YouTube URL directly from the HTML form to trigger the download process.

7. **Submit a YouTube URL to download:**
   - Enter a valid YouTube URL in the form and click "Download".
   - The video will be downloaded to your default "Downloads" folder.
   - The status of the download will be displayed on the web page.

Here are the screenshots of the final outputs. Feel free to provide any additional insights or feedback on this project.

![image](https://github.com/user-attachments/assets/f68f5a47-7f4e-4259-8b25-ab008ed3a04b)


![image](https://github.com/user-attachments/assets/6a601c9b-942a-4497-b716-625997d2b410)

