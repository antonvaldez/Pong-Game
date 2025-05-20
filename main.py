from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from borders import Borders

import time

screen = Screen()
screen.title("Anton's Pong Game")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

borders = Borders()

borders.draw_borders()

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game = True
while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()

    if 320 < ball.xcor() < 350 and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50 and ball.x_move > 0 or -350 < ball.xcor() < -320 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50 and ball.x_move < 0:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.center()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.center()
        scoreboard.right_point()

screen.exitonclick()