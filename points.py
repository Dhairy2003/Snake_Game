from turtle import Turtle
from random import randint


class Point(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5 , stretch_len=0.5)
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.new_loc()

    def new_loc(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)

