starting_postion= [(0,0),(-20,0), (-40,0)]
Move_distance= 10

from turtle import Turtle

class Snake:


    def __init__(self):

        self.segments= []
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):

        for _ in starting_postion:
            self.segment = Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(_)
            self.segments.append(self.segment)

    
    def move_snake(self):

        for seg_num in range(len(self.segments)-1, 0, -1):

            new_x= self.segments[seg_num - 1].xcor()
            new_y= self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(Move_distance)
    
    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(360)
       
         