from turtle import Turtle, Screen

t = Turtle()

for i in range(50):

    t.forward(5)
    t.up()
    t.forward(5)
    t.down()

screen = Screen()
screen.exitonclick()