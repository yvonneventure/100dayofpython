from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)
## python decorator function start with @
app = Flask(__name__)
# '/' is homepage
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"




def makeitbold(function):
    def bold():
        return "<b>"+function()+"</b>"
    return bold

@app.route("/<path:name>/profile")
def username(name):
    return f'hello {name}'


@app.route('/bye')
@makeitbold
def bye():
    return "Goodbye!"


if __name__ == '__main__':
    app.run(debug=True)