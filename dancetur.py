import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(10)

# Define a function to make the turtle move and change colors
def dance():
    # Move the turtle forward and backward
    for _ in range(2):
        t.forward(100)
        t.backward(100)
    
    # Rotate the turtle left and right
    for _ in range(2):
        t.left(45)
        t.right(45)
    
    # Change the turtle's color
    t.color("red")
    
    # Move the turtle in a circle
    t.circle(50)
    
    # Change the turtle's color again
    t.color("blue")
    
    # Move the turtle in a square
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Call the dance function multiple times to make the turtle dance
for _ in range(5):
    dance()

# Exit the turtle graphics window when clicked
turtle.exitonclick()
