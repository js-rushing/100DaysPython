from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def emphasize(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/bye")
@make_bold
@emphasize
@underline
def bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1 style='text-align: center'>Hello {name}, you are {number}!</h1>"


@app.route("/puppy")
def scone():
    return "<p>Puppy</p>" \
           "<img src='https://media.giphy.com/media/V3Z76ctCO3jG0/giphy.gif' />"


if __name__ == "__main__":
    app.run(debug=True)
