from flask import Flask
from random import randrange

app = Flask(__name__)
correct_number = randrange(10)

print(correct_number)


@app.route('/')
def main():
    return (f"<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route('/<int:guess_number>')
def guess(guess_number):
    if guess_number < correct_number:
        return (f"<h1 style='color: red'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    elif guess_number > correct_number:
        return (f"<h1 style='color: purple'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        return (f"<h1 style='color: green'>Correct!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
