from flask import Flask, render_template, request
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        header_text = 'Contact Me'

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        header_text = 'Successfully Sent Your Message'
        print(f'Username: {username}\nEmail: {email}\nPhone: {phone}\nMessage: {message}')

    return render_template('contact.html', header_text=header_text)


@app.route('/post/<post_id>')
def post(post_id):
    posts = requests.get(url=API_ENDPOINT).json()
    post_item = [item for item in posts if item['id'] == int(post_id)]
    print(post_item[0])
    return render_template('post.html', post=post_item[0])


if __name__ == '__main__':
    app.run(debug=True)
