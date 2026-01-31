from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220,260)
        self.level = 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", False, "center", FONT)




