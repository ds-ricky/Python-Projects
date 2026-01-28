from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(700, 500)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

y_value= -120.00
for pos in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[pos])
    tim.goto(x=-330, y=y_value)
    y_value += 40
    turtles.append(tim)

user = screen.textinput(title="Make your bet.", prompt="Which Turtle will win the race. Enter a color: ")

race_completed = False
while not race_completed:
    for turtle in turtles:
        if turtle.xcor() > 330:
            race_completed = True
            turtle_color = turtle.pencolor()
            if user == turtle_color:
                print(f"You've won! The {turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle_color} turtle is the winner!")
        distance = random.randint(0, 15)
        turtle.forward(distance)

screen.exitonclick()