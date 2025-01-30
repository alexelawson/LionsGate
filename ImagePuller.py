import os
import requests
import schedule
import time
from datetime import datetime

# URL of the image
IMAGE_URL = "https://cache.drivebc.ca/bchighwaycam/pub/cameras/18.jpg"  # Replace with actual URL
SAVE_DIR = "/Users/alexlawson/Documents/GitHub/LionsGate/Images"  # Folder to save images

# Ensure directory exists
os.makedirs(SAVE_DIR, exist_ok=True)

def download_image():
    """Downloads the image and saves it with a timestamp."""
    try:
        response = requests.get(IMAGE_URL, stream=True)
        if response.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = os.path.join(SAVE_DIR, f"image_{timestamp}.jpg")
            
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            print(f"Image saved: {image_path}")
        else:
            print(f"Failed to download image, status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {e}")

# Schedule the task every 15 minutes
schedule.every(15).minutes.do(download_image)

print("Image download script running... Press Ctrl+C to stop.")
download_image()  # Run once at start

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait 1 minute before checking schedule again