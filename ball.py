from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = random.choice([-10, 10])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1.2

    def center(self):
        self.x_move = 10 * (-1 if self.x_move > 0 else 1)
        self.y_move = random.choice([-10, 10])
        self.goto(0,0)
