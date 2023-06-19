import turtle
import random

t = turtle.Turtle()



def colorsss():
  r= random.randint(0, 255)
  g= random.randint(0, 255)
  b= random.randint(0, 255)
  random_color= (r,g ,b)
  return random_color

turtle.colormode(255)
t.speed("fastest")

default_radius=100
default_rotate=2
is_done=True


while is_done:


    t.circle(default_radius)
    t.left(default_rotate)
    default_rotate+=2
    t.color(colorsss())



  




  