from flask import Flask

# The __name__ variable holds the name of the current module.
# Flask uses it to determine the root path of your application.
# If this file is run directly, __name__ will be "__main__".
# If it's imported as a module, __name__ will be the module's name.
app = Flask(__name__)

print(__name__)  # Prints "__main__" if the file is executed directly

#Function Decorators
def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}<u>'
    return wrapper_function

def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}<b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}<em>'
    return wrapper_function

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>'\
           '<p>This is a paragraph.</p>'\
           '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGxmcTk1a3UxOGduaHI2NGswbGhwc20wNWtodG1wenRtbGJxczcxeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vFKqnCdLPNOKc/giphy.gif" width=200>'

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old."

# This block ensures the app runs only when executed directly,
# and not when the file is imported as a module in another script.
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode to auto-reload
