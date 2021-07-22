from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import DataRequired, url
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(256), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(120), nullable=False)
    ranking = db.Column(db.Integer)
    img_url = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    year = StringField('Release Year', validators=[DataRequired()])
    description = TextField('Description',
                            validators=[DataRequired()],
                            render_kw={'style': 'height: 8rem'})
    rating = StringField('Rating out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Brief Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired(), url()])
    submit = SubmitField('Add Movie')


class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10',
                         validators=[DataRequired()])
    review = StringField('Your Review',
                         validators=[DataRequired()])
    submit = SubmitField('Done')


# db.create_all()
#
# movie1 = Movie(title='Phone Booth',
#                year=2002,
#                description='Publicist Stuart Shepard finds himself '
#                            'trapped in a phone booth, pinned down by '
#                            'an extortionist\'s sniper rifle. Unable '
#                            'to leave or receive outside help, Stuart\'s '
#                            'negotiation with the caller leads to a '
#                            'jaw-dropping climax.',
#                rating=7.3,
#                review='My favourite character was the caller.',
#                img_url='https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg')
# db.session.add(movie1)
# db.session.commit()


@app.route("/")
def home():
    # all_movies = db.session.query(Movie).all()
    all_movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    print(all_movies)
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_movie = Movie(title=form.title.data,
                          year=form.year.data,
                          description=form.description.data,
                          rating=form.rating.data,
                          review=form.review.data,
                          img_url=form.img_url.data)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('movie_id')
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        movie_to_update = Movie.query.filter_by(id=movie_id).first()
        movie_to_update.rating = rating
        movie_to_update.review = review
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('movie_id')
    movie_to_delete = Movie.query.filter_by(id=movie_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
