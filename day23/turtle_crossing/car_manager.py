from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self):
        num = random.randint(1, 6)
        if num == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y_random = random.randint(-250, 250)
            car.setpos(300, y_random)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
