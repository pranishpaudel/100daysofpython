import turtle

def draw_circle():
    turtle.speed(0)  # Set the speed of the turtle (0 is the fastest)
    turtle.bgcolor("black")  # Set the background color to black
    
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  # List of colors
    
    while True:  # Loop infinitely
        for color in colors:
            turtle.pencolor(color)  # Set the pen color
            turtle.circle(100)  # Draw a circle with radius 100
