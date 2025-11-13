from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90
FONT = ("Courier", 24, "normal")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.new_frame()


    def move_up(self):

        self.forward(MOVE_DISTANCE)

    def new_frame(self):
        self.setheading(NORTH)
        self.goto(STARTING_POSITION)

    def game_over(self, score):
        self.goto(0,0)
        self.write(f"GAME OVER! \n score: {score}", move=False, align='center', font=FONT)






