import turtle
import random

# Create the turtle
t = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.setup(500, 500)

# Set the turtle speed
t.speed(1)

# Function to move the turtle randomly
def move_randomly():
    # Generate random angles and distances
    angle = random.randint(0, 360)
    distance = random.randint(10, 50)

    # Move the turtle
    t.right(angle)
    t.forward(distance)

# Set up the event listener
screen.onkey(move_randomly, 'space')
screen.listen()

# Start the main event loop
turtle.mainloop()
