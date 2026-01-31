from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.paddle(position)


    def paddle(self,positition):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(postition)
    
    def go_up(self):
        self.y_cor = self.ycor() + 20
        self.goto(x=self.xcor(), y=self.y_cor)


    def go_down(self):
        self.y_cor = self.ycor() - 20
        self.goto(x=self.xcor(), y=self.y_cor)
