from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.new_xcor = 0
        self.new_ycor = -280
        self.goto(self.new_xcor, self.new_ycor)

    def move(self):
        self.forward(20)

    def move_left(self):
        self.new_xcor -= 20
        self.goto(self.new_xcor, self.ycor())

    def move_right(self):
        self.new_xcor += 20
        self.goto(self.new_xcor, self.ycor())
