from turtle import Turtle, Screen
tim= Turtle()
screen= Screen()

def move_forward():
  tim.forward(5)

def move_backward():
  tim.forward(-5)
  
def move_anticlock():
  tim.left(5)

def move_clock():
  tim.right(5)

def clear():
  tim.clear()
  
screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_anticlock)
screen.onkey(key="D", fun=move_clock)
screen.onkey(key="C", fun=clear)
