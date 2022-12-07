import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard=Scoreboard()

screen.listen()
events = {"Up": player.move}
for key, func in events.items():
    screen.onkey(func, key)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect collision between player and cars
    for car in car_manager.cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()
            break

    # detect the player reaches the goal
    if player.reach_goal():
        player.start_position()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
