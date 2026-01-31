from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.no_animation


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_over = False
while not game_over:
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed()

    if ball.xcor() > 390: 
        ball.reset_ball()
        scoreboard.right_point()

    if ball.xcor() < -390:
        ball.reset_ball()
        scoreboard.left_point()
    

screen.exitonclick()