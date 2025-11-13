from turtle import Turtle, Screen
import random
#
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
#
# for _ in range(5):
#     tim.forward(100)
#     tim.right(90)
#
# screen = Screen()
# screen.exitonclick()

import turtle as t
# import heroes
#
# random_hero = heroes.gen()
#
# print(random_hero)


# Create a Turtle object (instance of the Turtle class)
# t = Turtle()
#
# # Draw a dashed line
# for _ in range(10):  # Adjust range for desired length
#     t.forward(10)    # Draw a segment
#     t.penup()        # Lift pen to stop drawing
#     t.forward(10)    # Move forward without drawing
#     t.pendown()      # Put pen down to resume drawing



for sides in range(3,10 +1):
    # Set color mode to 255 for RGB values
    t.getscreen().colormode(255)

    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    for _ in range(sides):
        t.color(r, g, b)
        t.right(360/sides)
        t.forward(100)



screen = Screen()
screen.exitonclick()