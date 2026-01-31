from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def new_cars(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.setheading(180)
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.car_list.append(car)
            self.car_movement()

    def car_movement(self):
        for car in self.car_list:
            car.forward(self.current_speed)

    def incr_speed(self):
        self.current_speed += MOVE_INCREMENT

