from turtle import Turtle

CORDS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.lst = []
        self.create()

    def create(self):
        for x in CORDS:
            self.add_segment(x)

    def add_segment(self, position):
        obj = Turtle("square")
        obj.penup()
        obj.color("white")
        obj.goto(position)
        self.lst.append(obj)

    def extend(self):
        #position function is a function by turtle
        self.add_segment(self.lst[-1].position())

    def move(self):
        for i in range(len(self.lst) - 1, 0, -1):
            new_x = self.lst[i - 1].xcor()
            new_y = self.lst[i - 1].ycor()
            self.lst[i].goto(new_x, new_y)
        self.lst[0].forward(SPEED)

    def up(self):
        if self.lst[0].heading() != DOWN:
            self.lst[0].setheading(UP)

    def down(self):
        if self.lst[0].heading() != UP:
            self.lst[0].setheading(DOWN)

    def left(self):
        if self.lst[0].heading() != RIGHT:
            self.lst[0].setheading(LEFT)

    def right(self):
        if self.lst[0].heading() != LEFT:
            self.lst[0].setheading(RIGHT)
