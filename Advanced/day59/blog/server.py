from flask import Flask, render_template
import requests

API_ENDPOINT = 'https://api.npoint.io/8615618024037d9a88ac'


app = Flask(__name__)


@app.route('/')
def home():
    posts = requests.get(url=API_ENDPOINT).json()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<post_id>')
def post(post_id):
    posts = requests.get(url=API_ENDPOINT).json()
    post_item = [item for item in posts if item['id'] == int(post_id)]
    print(post_item[0])
    return render_template('post.html', post=post_item[0])


if __name__ == '__main__':
    app.run(debug=True)
