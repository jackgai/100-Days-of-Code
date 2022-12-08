from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def read_score():
    with open("data.txt", mode="r") as file:
        content = file.read()
    if len(content) < 1:
        return 0
    return int(content)


def write_score(score):
    with open("data.txt", mode="w") as file:
        file.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_score()
        print(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}　High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.high_score = max(self.score, self.high_score)
        self.score = 0
        self.update_scoreboard()
        write_score(self.high_score)
