import turtle
import random

# Create a turtle and set its speed
dancer = turtle.Turtle()
dancer.speed(0)

# Function to generate a random color
def random_color():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    return random.choice(colors)

# Function to make the turtle dance
def dance():
    # Randomly change the turtle's color
    dancer.color(random_color())

    # Move the turtle forward and turn it randomly
    dancer.forward(100)
    dancer.right(random.randint(0, 360))

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Make the turtle dance
while True:
    dance()

# Close the turtle graphics window
turtle.done()
