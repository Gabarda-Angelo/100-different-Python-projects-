import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.display_score()

    car_manager.create_car()
    car_manager.move_cars()


    # detect collision with the player
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            player.game_over(scoreboard.score)
            game_is_on = False


    #adding next level
    if player.ycor() > 280:
        player.new_frame()
        scoreboard.increase_score()
        car_manager.car_increase_speed()
        # car_spawn_interval = max(3, car_spawn_interval - 1)  # Increase spawn rate


    # Remove cars that move off-screen
    car_list = [car for car in car_manager.all_cars if car.xcor() > -320]


screen.exitonclick()