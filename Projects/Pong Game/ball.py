from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = [1,2,3,4,5,6,7,8,9,10]
        self.index = 0

    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.speed(1)
        self.index = 0
        self.bounce_x()


    def increase_speed(self):
        if self.index < len(self.ball_speed) - 1:
            self.index += 1
        self.speed(self.index)
        