from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_list = []
        self.starting_position()
        self.head = self.snake_list[0]


    def starting_position(self):
        for pos in POSITION:
            self.body_adding(pos)


    def body_adding(self, pos):
        snake = Turtle(shape="square")
        snake.color(255, 255, 255)
        snake.penup()
        snake.goto(pos)
        self.snake_list.append(snake)


    def extend_body(self):
        self.body_adding(self.snake_list[-1].position())


    def move(self):
        for give_position in range(len(self.snake_list) - 1, 0, -1):
            x_cor = self.snake_list[give_position - 1].xcor()
            y_cor = self.snake_list[give_position - 1].ycor()
            self.snake_list[give_position].goto(x=x_cor, y=y_cor)
        self.head.forward(DISTANCE)


    def reset(self):
        for snake in self.snake_list:
            snake.goto(1000, 1000)
        self.snake_list.clear()
        self.starting_position()
        self.head = self.snake_list[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
