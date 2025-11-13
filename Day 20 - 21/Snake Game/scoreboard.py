from turtle import Turtle
ALGINMENT ="center"
FONT = ("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 250)  # Position scoreboard
        self.hideturtle()

    def increase_score(self):
        self.score +=1

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='center', font=FONT)

