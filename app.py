import os
import requests
import schedule
import time
from flask import Flask, send_from_directory, render_template
from datetime import datetime
import threading

# Flask App Setup
app = Flask(__name__)

# Image Settings
IMAGE_URL = "https://cache.drivebc.ca/bchighwaycam/pub/cameras/18.jpg"  # Replace with actual image URL
SAVE_DIR = "static/images"
LATEST_IMAGE_PATH = os.path.join(SAVE_DIR, "latest.jpg")

# Ensure directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def download_image():
    """Downloads the image and updates the latest.jpg file."""
    try:
        response = requests.get(IMAGE_URL, stream=True)
        if response.status_code == 200:
            with open(LATEST_IMAGE_PATH, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Failed to download image, status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Schedule the task every 15 minutes
schedule.every(15).minutes.do(download_image)

def run_scheduler():
    """Runs the scheduled tasks in a separate thread."""
    while True:
        schedule.run_pending()
        time.sleep(60)

# Start scheduler in a separate thread
threading.Thread(target=run_scheduler, daemon=True).start()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/latest-image")
def latest_image():
    return send_from_directory(SAVE_DIR, "latest.jpg", as_attachment=False)

if __name__ == "__main__":
    # Download image once at start
    download_image()
    app.run(debug=True, host="0.0.0.0", port=5001)
