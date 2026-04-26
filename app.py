from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/danspotting")
def danspotting():
    return render_template("danspotting.html")

@app.route("/food")
def food():
    food_dir = os.path.join(app.static_folder, "food")
    photos = []
    if os.path.exists(food_dir):
        photos = [
            {
                "filename": f,
                "label": os.path.splitext(f)[0].replace("-", " ").replace("_", " ").title(),
                "full": "food/" + f
            }
            for f in os.listdir(food_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        ]
    return render_template("food.html", photos=photos)

if __name__ == "__main__":
    app.run(debug=True)