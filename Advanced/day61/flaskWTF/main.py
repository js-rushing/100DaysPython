from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from config import SECRET

app = Flask(__name__)
Bootstrap(app)

app.secret_key = SECRET


class LoginForm(FlaskForm):
    email = StringField(label='Email',
                        validators=[DataRequired(),
                                    Length(min=6, message=(u'Email is too short.')),
                                    Email(message='Invalid email address')],
                        render_kw={'style': 'width: 40rem'})
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         Length(min=6, message=(u'Password is too short'))],
                             render_kw={'style': 'width: 40rem'})
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    form.validate_on_submit()

    # Checks if valid form submitted
    # Will be true if method == post
    # and form data is valid
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
