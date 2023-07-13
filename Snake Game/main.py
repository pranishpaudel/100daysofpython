from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)



snake= Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




food= Food()
scoreboard= Scoreboard()



is_game_on= True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    if snake.head.distance(food)<15:
       
       food.refresh()
       scoreboard.increase()
    

screen.exitonclick()