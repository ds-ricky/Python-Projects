import turtle
import pandas


screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_data = data.state.to_list()
correct_guess = []

while len(correct_guess) < 50:
    guess = screen.textinput(f"{len(correct_guess)}/50 Guess the State.", "What's the another State's name?").title()
    if guess == "Exit":
        not_guess = []
        for state in states_data:
            if state not in correct_guess:
                not_guess.append(state)
        new_data = pandas.DataFrame(not_guess)
        new_data.to_csv("States_to_learn.csv")
        break
    if guess in states_data:
        correct_guess.append(guess)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_coordinate = data[data.state == guess]
        t.goto(state_coordinate.x.item(), state_coordinate.y.item())
        t.write(state_coordinate.state.item())

