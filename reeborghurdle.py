#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

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

for char in range (1,7):
    jump()



