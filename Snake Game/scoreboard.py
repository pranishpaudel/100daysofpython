from turtle import Turtle
NON= None

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.score=0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update_score()