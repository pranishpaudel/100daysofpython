starting_postion= [(0,0),(-20,0), (-40,0)]
Move_distance= 10
UP= 90
DOWN= 270
LEFT=180
RIGHT= 0

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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
       if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
       
         