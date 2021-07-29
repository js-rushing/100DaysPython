import sqlalchemy.orm.exc
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
from pprint import pprint

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all", methods=["GET"])
def all_records():
    all_rows = db.session.query(Cafe).all()
    cafe_list = []
    for row in all_rows:
        row_dict = row.to_dict()
        cafe_list.append(row_dict)
    cafe_dict = {"cafes": cafe_list}
    data = jsonify(cafe_dict)
    return data


@app.route("/search", methods=["GET"])
def search():
    if request.args.get('loc'):
        loc = request.args.get('loc')
    else:
        error = {
            "error": {
                "Param Error": "Incorrect search parameter"
            }
        }
        return jsonify(error)
    cafes = Cafe.query.filter_by(location=loc)
    cafe_list = []
    for cafe in cafes:
        cafe_list.append(cafe.to_dict())
    if len(cafe_list) == 0:
        error = {
            "error": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        }
        return jsonify(error)
    else:
        cafe_dict = {"cafes": cafe_list}
        data = jsonify(cafe_dict)

        return data


@app.route("/random", methods=["GET"])
def random():
    row_count = db.session.query(Cafe).count()
    random_record = Cafe.query.get(randint(1, row_count))
    data = jsonify(random_record.to_dict())
    return data


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get('name')
    map_url = request.form.get('map_url')
    img_url = request.form.get('img_url')
    location = request.form.get('location')
    has_sockets = bool(int(request.form.get('has_sockets')))
    has_toilet = bool(int(request.form.get('has_toilet')))
    has_wifi = bool(int(request.form.get('has_wifi')))
    can_take_calls = bool(int(request.form.get('can_take_calls')))
    seats = request.form.get('seats')
    coffee_price = request.form.get('coffee_price')
    new_cafe = Cafe(name=name,
                    map_url=map_url,
                    img_url=img_url,
                    location=location,
                    has_sockets=has_sockets,
                    has_toilet=has_toilet,
                    has_wifi=has_wifi,
                    can_take_calls=can_take_calls,
                    seats=seats,
                    coffee_price=coffee_price)
    pprint(new_cafe.to_dict())
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response": {
        "success": "Successfully added the new cafe."
    }})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
    try:
        cafe_to_update.coffee_price = request.args.get('new_price')
    except AttributeError:
        data = {
            "error": {
                "Not Found": "Sorry, a cafe with that id was not found in the database."
            }
        }
        return jsonify(data)
    db.session.commit()
    data = {
        "success": "Successfully updated the price."
    }
    return jsonify(data)


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == "TopSecretAPIKey":
        cafe_to_delete = Cafe.query.filter_by(id=cafe_id).first()
        try:
            db.session.delete(cafe_to_delete)
            db.session.commit()
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            data = {
                "error": {
                    "Not Found": "Sorry, a cafe with that id was not found in the database."
                }
            }
            return jsonify(data)
        data = {
            "success": "Successfully deleted cafe from database."
        }
        return jsonify(data)
    else:
        data = {
            "status": "403",
            "error": {
                "Not Authorized": "You are not authorized to make this request."
            }
        }
        return jsonify(data)


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
