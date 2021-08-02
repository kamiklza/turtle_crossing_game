from turtle import Turtle
import random
import time
colors = ["yellow", "green", "red", "purple", "pink", "blue"]

class Obstacle():
    def __init__(self):
        self.segments = []
        self.xcor = 290

    def create_obstacle(self):
        new_obstacle = Turtle()
        new_obstacle.color(random.choice(colors))
        new_obstacle.penup()
        new_obstacle.shape("square")
        new_obstacle.shapesize(stretch_wid=0.5, stretch_len=random.randrange(1, 3))
        new_ycor = random.randrange(-250, 270)
        new_obstacle.goto(self.xcor, new_ycor)
        self.segments.append(new_obstacle)
        self.xcor += random.randint(20, 50)




    def move(self, speed):
        for segment in self.segments:
            segment.goto(segment.xcor() - speed, segment.ycor())





