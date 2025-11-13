import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forwards():
    tim.forward(20)
def back_wards():
    tim.backward(20)
def counter_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def clear_drawings():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=back_wards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawings)
screen.exitonclick()

