from turtle import Turtle

ORIGINAL_SPEED = 0.1


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.position = position
        self.setpos(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = ORIGINAL_SPEED

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move = -self.x_move

    def reset_position(self):
        self.setpos(self.position)
        self.move_speed = ORIGINAL_SPEED
        self.bounce_x()
