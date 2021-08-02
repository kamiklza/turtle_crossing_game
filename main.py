
from turtle import Turtle, Screen
from player import Player
from level_tracker import Level
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
level = Level()
obstacle = Obstacle()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


is_game_on = True
while is_game_on:
    time.sleep(0.05)
    obstacle.create_obstacle()
    screen.update()
    obstacle.move()

    if player.ycor() > 280:
        player.reset_player()
        level.next_level()
        obstacle.move_faster()
        player.speed_up()

    for segment in obstacle.segments:
        if player.distance(segment) < 18:
            player.reset_player()
            level.reset_level()
            obstacle.reset_speed()


screen.exitonclick()