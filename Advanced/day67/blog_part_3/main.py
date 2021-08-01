from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db.session.query(BlogPost).all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    date = dt.date.today().strftime('%B %d, %Y')
    print(date)
    form = CreatePostForm()
    if form.validate_on_submit():
        post_to_add = BlogPost(title=form.title.data,
                               subtitle=form.subtitle.data,
                               date=date,
                               body=form.body.data,
                               author=form.author.data,
                               img_url=form.img_url.data)
        db.session.add(post_to_add)
        db.session.commit()
        return redirect(url_for('show_post', index=db.session.query(BlogPost).count()))
    return render_template('make-post.html', form=form, headline='New Post')


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = BlogPost.query.filter_by(id=post_id).first()
    date = post_to_edit.date
    form = CreatePostForm(title=post_to_edit.title,
                          subtitle=post_to_edit.subtitle,
                          body=post_to_edit.body,
                          author=post_to_edit.author,
                          img_url=post_to_edit.img_url)
    if form.validate_on_submit():
        post_to_edit.title = form.title.data
        post_to_edit.subtitle = form.subtitle.data
        post_to_edit.date = date
        post_to_edit.body = form.body.data
        post_to_edit.author = form.author.data
        post_to_edit.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('show_post', index=post_to_edit.id))
    return render_template('make-post.html', form=form, headline='Edit Post')


@app.route("/delete/<int:index>")
def delete(index):
    post_to_delete = BlogPost.query.get(index)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
