from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height =400)

colors = ["red", "orange", "yellow", "green", "blue","violet", "purple"]
user_bet = screen.textinput(title="Make your bet" , prompt=f"Which turtle would you like to move{colors}? Enter a color: ")
y_positions = [-70, -40, -10, 20, 50, 80, 110]

turtles  = []

for turtle_index in range(0, 7):

    new_turtles = Turtle(shape = "turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_positions[turtle_index])

    turtles.append(new_turtles)



race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_turtle_color = turtle.pencolor()
            if user_bet == winning_turtle_color:
                print(f"you've won! the {winning_turtle_color} Turtle wins!")
            else:
                print(f"you've lost! the {winning_turtle_color} Turtle wins!")

        random_steps = random.randint(1, 10)
        turtle.forward(random_steps)




screen.exitonclick()