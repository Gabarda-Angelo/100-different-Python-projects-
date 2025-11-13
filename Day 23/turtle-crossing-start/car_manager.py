from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LOOK_WEST = 180



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        '''create car in random circumstances only, and not every iteration'''
        if random_chance == 1:
            new_car = Turtle("square")
            x_cor = 280
            y_cor = random.randint(-250, 250)
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(LOOK_WEST)
            new_car.goto(x_cor, y_cor)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_increase_speed(self):
        self.car_speed += MOVE_INCREMENT






