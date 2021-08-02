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
        self.start_speed = 20

    def move_up(self):
        self.forward(self.start_speed)

    def move_down(self):
        self.backward(self.start_speed)

    def move_left(self):
        self.new_xcor -= self.start_speed
        self.goto(self.new_xcor, self.ycor())

    def move_right(self):
        self.new_xcor += self.start_speed
        self.goto(self.new_xcor, self.ycor())

    def reset_player(self):
        self.goto(self.new_xcor, self.new_ycor)

    def speed_up(self):
        self.start_speed += 1

    def reset_speed(self):
        self.start_speed = 10
