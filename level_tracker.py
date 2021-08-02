from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 240)
        self.level = 0
        self.current_level()


    def current_level(self):
        self.write(f"Level: {self.level}", move=False, font=("Arial", 40, "normal"))

    def next_level(self):
        self.clear()
        self.level += 1
        self.current_level()

