from functools import wraps

from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_gravatar import Gravatar
from forms import CreatePostForm, CreateLoginForm, CreateRegistrationForm, CreateCommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def logged():
    return current_user.is_authenticated


def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            if current_user.role != 'admin':
                return abort(403)
            return function(*args, **kwargs)
        except AttributeError:
            return abort(403)
    return wrapper


def get_role():
    role = 'anon'
    if logged():
        role = current_user.role
    return role


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    role = db.Column(db.String(25), nullable=False, default='user')


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("Comment", back_populates="original_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = relationship("User", back_populates="comments")
    original_post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
    original_post = relationship("BlogPost", back_populates="comments")
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)


# db.create_all()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html",
                           all_posts=posts,
                           logged_in=logged(),
                           role=get_role(),
                           current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = CreateRegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = generate_password_hash(password=form.password.data,
                                          method='pbkdf2:sha256',
                                          salt_length=8)
        if not User.query.filter_by(email=email).first():
            user = User(name=name,
                        email=email,
                        password=password)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful. You may participate in discussions.')
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            flash('Email already in database.')
            flash('Try logging in instead.')
            return redirect(url_for('login'))
    return render_template("register.html", form=form, logged_in=logged())


@app.route('/login', methods=["GET", "POST"])
def login():
    form = CreateLoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = User.query.filter_by(email=email).first()
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Login successful.')
                return redirect(url_for('get_all_posts'))
            else:
                flash('Incorrect password. Please try again.')
                return redirect(url_for('login'))
        except AttributeError:
            flash('Email not in database.')
            return redirect(url_for('register'))
    return render_template("login.html", form=form, logged_in=logged())


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out.')
    else:
        flash('You\'ve been logged out this whole time, bro.')
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    all_comments = Comment.query.filter_by(original_post_id=requested_post.id).all()
    form = CreateCommentForm()
    if form.validate_on_submit():
        comment = Comment(date=date.today().strftime("%B %d, %Y"),
                          author=current_user,
                          original_post=requested_post,
                          body=form.body.data)
        db.session.add(comment)
        db.session.commit()
    return render_template("post.html",
                           post=requested_post,
                           all_comments=all_comments,
                           logged_in=logged(),
                           role=get_role(),
                           form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", logged_in=logged())


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, logged_in=logged())


@app.route("/edit-post/<int:post_id>")
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, logged_in=logged())


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
