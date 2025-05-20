from turtle import Turtle

class Borders(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(4)
        self.speed("fastest")

    def draw_borders(self):
        self.penup()
        self.goto(-390, 290)
        self.pendown()
        self.color("red")
        self.forward(780)

        self.penup()
        self.goto(390, 290)
        self.setheading(-90)
        self.color("green")
        self.pendown()
        self.forward(580)

        self.penup()
        self.goto(390, -290)
        self.setheading(180)
        self.color("red")
        self.pendown()
        self.forward(780)

        self.penup()
        self.goto(-390, -290)
        self.setheading(90)
        self.color("blue")
        self.pendown()
        self.forward(580)