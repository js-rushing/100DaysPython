from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = Post().posts


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    post = posts[int(blog_id) - 1]
    print(post)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
