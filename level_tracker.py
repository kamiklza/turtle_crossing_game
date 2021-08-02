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

    def reset_level(self):
        self.clear()
        self.level = 0
        self.current_level()

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.hideturtle()
        self.color("black")
        self.write("Game Over", move=False, align="center", font=("Arial", 30, "normal"))

