import turtle
import random

colors = ['white', 'yellow', 'orange', 'red', 'pink', 'purple', 'blue', 'green', 'brown', 'black']
t = turtle.Turtle()
t.pensize(5)

direction= [0,90,180,270]
is_done=True
while is_done:
  t.color(random.choice(colors))
  t.forward(30)
  t.setheading(random.choice(direction))

  




  