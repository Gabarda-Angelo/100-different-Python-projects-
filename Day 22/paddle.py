from turtle import Turtle

'''turtle pixels by default is 20, therefore the width is 20 x 100'''
PADDLE_HEIGHT = 1
PADDLE_WIDTH = 5
MOVE_DISTANCE = 20  # Smaller steps for smoother movement
SCREEN_HEIGHT = 600  # Default turtle screen height (adjust if different)

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.turtlesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.shape("square")
        self.color("white")
        self.PADDLE_INIT_POSITION = position
        self.penup()
        self.goto(self.PADDLE_INIT_POSITION)

    def go_up(self):
        # Calculate new y-coordinate
        new_y = self.ycor() + MOVE_DISTANCE
        # Check if paddle stays within screen bounds (half paddle height = 50 pixels)
        if new_y + 25 < SCREEN_HEIGHT / 2:
            self.sety(new_y)

    def go_down(self):
        # Calculate new y-coordinate
        new_y = self.ycor() - MOVE_DISTANCE
        # Check if paddle stays within screen bounds (half paddle height = 50 pixels)
        if new_y - 25 > -SCREEN_HEIGHT / 2:
            self.sety(new_y)





