from turtle import Screen, Turtle
from day_21_paddle import Paddle
from day_21_ball import Ball
from day_21_scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
 
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ## detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ## needs to bounce
        ball.bounce_y()

    ## detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    ## detect when the right ball missess
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    ## detect when the left ball missess
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()