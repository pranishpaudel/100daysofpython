import turtle
from return_ordinates import Ordinates


screen= turtle.Screen()
screen.title("US Census Game")

image= "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

Turtle= turtle.Turtle("square")
Turtle.penup()
Turtle.hideturtle()
Turtle.speed("fastest")
Turtle.shapesize(2)

ordinates= Ordinates()

is_game_on= True
state_count= 1



while is_game_on:

    for _ in range (1,51):

        ask_state= screen.textinput(f"Guess the state: ({state_count} / 50)", "Whats another state")
        if ask_state in ordinates.all_state:
            x_coor= ordinates.x_coordinate(ask_state)
            y_coor= ordinates.y_coordinate(ask_state)
            Turtle.goto(x_coor,y_coor)
            Turtle.write(ask_state)
            state_count+=1
            if state_count == 50:
                is_game_on= False



screen.mainloop()