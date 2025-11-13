import turtle
from turtle import Turtle, Screen
import random

DISTANCE = 40
THICKNESS = 7

pagong = Turtle()
pagong.shape("turtle")
pagong.color("green")
pagong.speed("fastest")

# Set color mode to 255 for RGB values
pagong.getscreen().colormode(255)
# Generate random RGB values

DIRECTIONS = [0,90,180,270]


roaming = True

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_colors = (r, g, b)

    return random_colors



while roaming:
    pagong.setheading(random.choice(DIRECTIONS))
    pagong.pensize(THICKNESS)

    pagong.color(random_colors())
    pagong.forward(DISTANCE)



screen = Screen()
screen.exitonclick()