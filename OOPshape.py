import turtle
import random

turtleStar = turtle.Turtle()

pynum= [3,4,5,6,7,8,9,10]
pycolor= ["red","yellow","blue","purple","green","pink","red","grey"]

for numside0 in pynum:

  angle= 360/ numside0
  
  for _ in range(numside0):
    turtleStar.color(random.choice(pycolor))
    turtleStar.forward(100)
    turtleStar.right(angle)


  