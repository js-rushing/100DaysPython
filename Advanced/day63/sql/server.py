import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    review = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# db.create_all()

# book1 = Book(title='Harry Potter', author='J.K. Rowling', review=9.3)
# book2 = Book(title='Die Unendliche Geschichte',
#              author='Michael Ende',
#              review=9.5)
#
# db.session.add(book1)
# db.session.add(book2)
# db.session.commit()

# Read All Records
all_books = db.session.query(Book).all()
print(all_books)

# Read Single Record
# single_book = Book.query.filter_by(title="Harry Potter").first()
# print(single_book)

# Update Single Record
# book_to_update = Book.query.filter_by(title="Harry Potter and the Chamber of Secrets").first()
# book_to_update.title = "Harry Potter"
# db.session.commit()

# Delete Single Record
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()

# Read All Records
all_books = db.session.query(Book).all()
print(all_books)


# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE books ("
#                "id INTEGER PRIMARY KEY, "
#                "title varchar(250) NOT NULL UNIQUE, "
#                "author varchar(250) NOT NULL, "
#                "rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit()
