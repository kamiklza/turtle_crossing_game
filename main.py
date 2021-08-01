from turtle import Turtle, Screen
from player import Player
from level_tracker import Level
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
level = Level()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        print("Congrats")


screen.exitonclick()