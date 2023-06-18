import turtle

turtleStar = turtle.Turtle()
numside=5

angle= 360/ numside

for _ in range(numside):
  turtleStar.forward(100)
  turtleStar.right(angle)
  