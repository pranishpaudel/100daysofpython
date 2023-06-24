from turtle import Turtle, Screen

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segment_1= Turtle("square")
segment_1.color("white")
segment_2= Turtle("square")
segment_2.color("white")
segment_2.goto(-20,0)
segment_3= Turtle("square")
segment_3.color("white")
segment_3.goto(-40,0)
screen.exitonclick()