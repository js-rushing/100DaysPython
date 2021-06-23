from flask import Flask
import random

app = Flask(__name__)

NUM_LINKS = """
<div style='margin-top: 20px;'>
    <a href="http://localhost:5000/num/1" style='font-size: 30px;'>1</a>
    <a href="http://localhost:5000/num/2" style='font-size: 30px;'>2</a>
    <a href="http://localhost:5000/num/3" style='font-size: 30px;'>3</a>
    <a href="http://localhost:5000/num/4" style='font-size: 30px;'>4</a>
    <a href="http://localhost:5000/num/5" style='font-size: 30px;'>5</a>
    <a href="http://localhost:5000/num/6" style='font-size: 30px;'>6</a>
    <a href="http://localhost:5000/num/7" style='font-size: 30px;'>7</a>
    <a href="http://localhost:5000/num/8" style='font-size: 30px;'>8</a>
    <a href="http://localhost:5000/num/9" style='font-size: 30px;'>9</a>
</div>
"""

HOME_LINK = """
    <a href="http://localhost:5000" style='margin-top: 20px; font-size: 50px;'>Home</a>
"""


def new_rand_num():
    random_number = random.randint(1, 9)
    return random_number


def add_links(function):
    def wrapper(*args, **kwargs):
        if function.__name__ == "home":
            return f"{function(*args, **kwargs)}{NUM_LINKS}"
        else:
            return f"{function(*args, **kwargs)}{NUM_LINKS}{HOME_LINK}"
    wrapper.__name__ = function.__name__
    return wrapper


@app.route('/')
@add_links
def home():
    global rand_num
    rand_num = new_rand_num()
    return f"<h1>Guess a number between 1 and 9</h1>" \
           "<img src='https://media.giphy.com/media/Kehzyp9EFa2IYDte8P/giphy.gif' />" \
           # f"{NUM_LINKS}"


@app.route('/num/<int:num>')
@add_links
def number(num):
    global rand_num
    if int(num) == rand_num:
        return f"<h1 style='color: green;'>You're Right!</h1>" \
               f"<img src='https://media.giphy.com/media/ummeQH0c3jdm2o3Olp/giphy.gif' />" \
               # f"{NUM_LINKS}"
    elif int(num) < rand_num:
        return f"<h1 style='color: red;'>Too low.</h1>" \
               f"<img src='https://media.giphy.com/media/l0O9yanlMYzLFoa4M/giphy.gif' />" \
               # f"{NUM_LINKS}"
    elif int(num) > rand_num:
        return f"<h1 style='color: black;'>Too high.</h1>" \
               f"<img src='https://media.giphy.com/media/3muwhw9Jl2dNe/giphy.gif' />" \
               # f"{NUM_LINKS}"


rand_num = new_rand_num()

if __name__ == "__main__":
    app.run(debug=True)
