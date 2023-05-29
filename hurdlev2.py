
def right():
    turn_left()
    turn_left()
    turn_left()
def main():
 move()
 turn_left()
 move()
 right()
 move()
 right()
def jump():
  main()
  move()
  turn_left()

while not at_goal(): 
  jump()


