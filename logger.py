import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup Brave browser
brave_path = "path to brave"  # Change if you're on Windows/Mac
options = Options()
options.binary_location = brave_path
driver = webdriver.Chrome(options=options)

driver.get("https://www.youtube.com")

def get_video_info():
    try:
        video = driver.find_element("css selector", "video")
        paused = driver.execute_script("return arguments[0].paused;", video)
        if paused:
            current_time = int(driver.execute_script("return arguments[0].currentTime;", video))
            video_url = driver.current_url
            if "t=" not in video_url:
                if "?" in video_url:
                    video_url += f"&t={current_time}s"
                else:
                    video_url += f"?t={current_time}s"
            title = driver.title.replace(" - YouTube", "")
            return {"title": title, "url": video_url, "time": current_time, "saved_at": datetime.now().isoformat()}
    except:
        return None

def append_to_file(data, filename="saved_links.json"):
    try:
        with open(filename, "r") as f:
            existing = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []

    existing.append(data)
    with open(filename, "w") as f:
        json.dump(existing, f, indent=4)

print("🎬 Monitor started. Pause a YouTube video to save it...")
was_playing = True
while True:
    time.sleep(1)
    info = get_video_info()
    if info and was_playing:
        print(f"⏸️  Saved: {info['title']} at {info['time']}s")
        append_to_file(info)
        was_playing = False
    elif not info:
        was_playing = True
