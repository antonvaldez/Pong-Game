from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(x_cor, y_cor)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)