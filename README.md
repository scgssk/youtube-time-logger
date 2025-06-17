🎬 YouTube Pause Logger & Resume Tool

---

This tool lets you **pause a YouTube video** and automatically **save the current timestamp** to a local `JSON` file. Later, you can open an HTML page that lists:

- The **latest paused video** with a **"Continue Watching"** button  
- All previous paused videos as clickable links

It’s designed for **Brave browser users who don’t login or sync**, and **clear browser data on exit**.

---

**📂 Features**

✅ Save current YouTube video and timestamp when paused  
✅ View the latest saved video with a big resume button  
✅ Browse previously saved videos as links  
✅ No login or YouTube account required  
✅ Stores data in a local JSON file

---

**🧱 Tech Stack**

- 🐍 Python (Selenium for browser interaction)  
- 🦁 Brave Browser (Chrome-based)  
- 📄 HTML + JSON for UI and data  
- No third-party tracking or cloud dependencies

---

###🔧 Setup Instructions

## 1. Clone This Repo

git clone https://github.com/your-username/youtube-time-logger.git
cd youtube-time-logger

## 2. Create and Activate a Virtual Environment

python -m venv venv

# Activate:

# Windows

venv\Scripts\activate

# macOS/Linux

source venv/bin/activate


## 3. Install Dependencies

pip install selenium

## 4. Configure Brave Browser Path

Open `logger.py` and set the path to your Brave browser:

options.binary_location = "/usr/bin/brave-browser"  # Linux
# For Windows:
# options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

---

## ▶️ How to Use

### 1. Run the Logger Script

python youtube_pause_logger.py


> Keep this running in the background while watching YouTube.

Whenever you pause a video, it saves the title, URL, and timestamp to `saved_links.json`.

### 2. Open the Resume Viewer

Double-click or open `resume_youtube.html` in your browser.

* The **most recent paused video** appears with a **"Continue Watching"** button.
* All older saved videos appear as **clickable links**.

---


## 💡 Tips

* Brave’s strict tracking protection **does not block this tracker** — it's local and safe.
* You can use your real Brave profile to retain cookies, history, and extensions.
* If you don’t want to keep Python running all the time, consider packaging it as a tray app or cron job.

---

## ✅ To-Do / Improvements

* [ ] Add tags/notes to bookmarks
* [ ] Delete or edit saved entries
* [ ] Package as a browser extension
* [ ] Auto-run tracker in the background on boot

---
