
from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# -------------------------
# شمارنده بازدید
# -------------------------

counter_file = "counter.txt"

def get_counter():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("0")

    with open(counter_file, "r") as f:
        return int(f.read())

def increase_counter():
    count = get_counter() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count

# -------------------------
# صفحه اصلی
# -------------------------

@app.route("/")
def home():
    views = increase_counter()
    return render_template("welcome.html", views=views)

# -------------------------
# صفحه موزیک‌ها
# -------------------------

@app.route("/music")
def music():
    music_folder = os.path.join(app.static_folder, "music")
    songs = []

    if os.path.exists(music_folder):
        for file in os.listdir(music_folder):
            if file.endswith(".mp3"):
                songs.append(file)

    songs.sort()

    return render_template("music.html", songs=songs)

# -------------------------
# پلیر
# -------------------------

@app.route("/player/<song>")
def player(song):
    return render_template("player.html", song=song)

# -------------------------
# پخش تصادفی
# -------------------------

@app.route("/random")
def random_song():
    music_folder = os.path.join(app.static_folder, "music")
    songs = []

    if os.path.exists(music_folder):
        for file in os.listdir(music_folder):
            if file.endswith(".mp3"):
                songs.append(file)

    if not songs:
        return "هیچ موزیکی پیدا نشد."

    song = random.choice(songs)

    return render_template("player.html", song=song)

# -------------------------
# تماس با ما
# -------------------------

@app.route("/contact")
def contact():
    return render_template("contact.html")

# -------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)