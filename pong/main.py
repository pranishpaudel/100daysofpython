from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_Paddle=Paddle((350,0))
l_Paddle=Paddle((-350,0))

ball=Ball()
scoreboard= Scoreboard()



 

is_game_on= True







screen.listen()

screen.onkey(r_Paddle.go_up, "Up")
screen.onkey(r_Paddle.go_down, "Down")
screen.onkey(l_Paddle.go_up, "w")
screen.onkey(l_Paddle.go_down, "s")
default_speed=3

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    

    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce_y()
     

    #COLLOSION WOTH THE PADDELE

    if ball.distance(r_Paddle)<40 and ball.xcor()>320 or ball.distance(l_Paddle)<40 and ball.xcor()<-320:
        ball.bounce_x()
    


    if ball.xcor()>380:
        ball.reset_postion()
        scoreboard.left_score()
        ball.speed(default_speed)
        default_speed+=100

    if ball.xcor()<-380:
        ball.reset_postion()
        scoreboard.right_score()
        ball.speed(default_speed)
        default_speed+=100

screen.exitonclick()
