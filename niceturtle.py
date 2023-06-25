import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
t = turtle.Turtle()

# Set turtle properties
t.speed(0)  # Fastest speed
t.width(2)  # Pen width

# Define colors
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# Draw a colorful spiral pattern
for i in range(200):
    t.color(colors[i % len(colors)])
    t.forward(i)
    t.left(59)

# Exit on click
turtle.done()
