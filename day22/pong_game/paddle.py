from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(position)

    def go_up(self):
        y_new = self.ycor() + DISTANCE
        self.goto(self.xcor(), y_new)

    def go_down(self):
        y_new = self.ycor() - DISTANCE
        self.goto(self.xcor(), y_new)
