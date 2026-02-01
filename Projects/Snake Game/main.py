from turtle import Turtle,Screen
from food import Food
from scoreboard import Score
import time

from snake import Snake

jim = Turtle(shape="square")
screen = Screen()


screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refreshment()
        snake.extend_body()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for body in snake.snake_list[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()