from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class NewBookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Add Book')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = NewBookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data,
                        author=form.author.data,
                        rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()

        return redirect('/')
    return render_template('add.html', form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        new_rating = request.form['new_rating']
        book_to_update = Book.query.filter_by(id=book_id).first()
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        book_id = request.args.get('id')
        book = Book.query.filter_by(id=book_id).first()
        print(book)
    return render_template('edit.html', book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
