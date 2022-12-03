import time
from snake import Snake
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()

screen.listen()
event = {"Up": snake.up, "Down": snake.down, "Left": snake.left, "Right": snake.right}
for key, fun in event.items():
    screen.onkey(fun, key)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
