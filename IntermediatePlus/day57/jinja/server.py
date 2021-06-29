from flask import Flask, render_template
import random
import datetime as dt
import requests
import json
from config import AGIFY_API_URL, GENDERIZE_API_URL, BLOG_API_URL

app = Flask(__name__)


@app.route("/")
def index():
    random_number = random.randint(1, 10)
    year = dt.date.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=year)


@app.route("/info/<name>")
def info(name):
    name = name.title()
    age = requests.get(url=f"{AGIFY_API_URL}?name={name}").json()['age']
    gender = requests.get(url=f"{GENDERIZE_API_URL}?name={name}").json()['gender']
    return render_template("info.html", name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    res = requests.get(url=BLOG_API_URL)
    all_posts = res.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
