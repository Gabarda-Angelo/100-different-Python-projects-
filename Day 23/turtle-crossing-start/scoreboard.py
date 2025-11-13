from turtle import Turtle
FONT = ("Courier", 24, "normal")
BOARD_LOCATION = (-280,250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(BOARD_LOCATION)
        self.hideturtle()
        self.score = 0


    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='left', font=FONT)


    def increase_score(self):
        self.score += 1
