

from turtle import Turtle, Screen
import time
screen= Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

positioning= [(0,0),(-20,0), (-40,0)]

segments= []



for postion in positioning:
    segment= Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(postion)
    segments.append(segment)

is_game_on= True

while is_game_on:

    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) -1 , 0, -1):
       new_x= segments[seg_num - 1].xcor()
       new_y= segments[seg_num - 1].ycor()
       segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(20)
    segments[0].forward(20)






screen.exitonclick()


  