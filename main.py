from turtle import Turtle, Screen
from snake import Snake
from points import Point
from time import sleep
from Scoreboard import Score

ACCURACY = 15

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.title("Snake Game")

s = Snake()
p = Point()
sc = Score()

screen.onkey(key='Up', fun=s.up)
screen.onkey(key='Down', fun=s.down)
screen.onkey(key='Left', fun=s.left)
screen.onkey(key='Right', fun=s.right)

playing = True
while playing:
    screen.update()
    sleep(0.1)
    s.move()

    if s.lst[0].distance(p) < ACCURACY:
        s.extend()
        sc.score_inc()
        p.new_loc()

    if s.lst[0].xcor() > 295 or s.lst[0].xcor() < -295 or s.lst[0].ycor() > 295 or s.lst[0].ycor() < -295:
        sc.game_over()
        playing = False

    for x in s.lst[1:]:
        if s.lst[0].distance(x) < 10:
            sc.game_over()
            playing = False


screen.exitonclick()
