from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
from pprint import pprint
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), url()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 9:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating',
                         validators=[DataRequired()],
                         choices=['✘', '☕️', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField('Wifi Strength Rating',
                       validators=[DataRequired()],
                       choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power = SelectField('Power Socket Availability',
                        validators=[DataRequired()],
                        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_entry = f"{form.cafe.data}," \
                    f"{form.location.data}," \
                    f"{form.open.data}," \
                    f"{form.close.data}," \
                    f"{form.coffee.data}," \
                    f"{form.wifi.data}," \
                    f"{form.power.data}"
        with open('cafe-data.csv', mode='a') as file:
            file.write(f"\n{new_entry}")
        print("True")
        return redirect('/cafes')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    pprint(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
