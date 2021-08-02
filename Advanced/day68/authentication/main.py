from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from config import FILES_FOLDER, SECRET

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password = generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=8)
        user = User(name=name, email=email, password=password)
        if User.query.filter_by(email=email).first():
            flash('Email already in database.')
            flash('Try logging in instead.')
            return redirect(url_for('login'))
        else:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = User.query.filter_by(email=email).first()
            if check_password_hash(pwhash=user.password, password=password):
                # Login successful
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('secrets'))
            else:
                flash('Password incorrect, please try again.')
                return render_template('login.html')
        except AttributeError:
            flash('Email not in database.')
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html",
                           name=current_user.name,
                           logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return render_template('index.html', logged_in=current_user.is_authenticated)


@app.route('/download')
@login_required
def download():
    print(current_user.name)
    # return send_from_directory(app.config[FILES_FOLDER], 'cheat_sheet.pdf')
    return send_from_directory(directory='./static/files',
                               filename='cheat_sheet.pdf',
                               as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
