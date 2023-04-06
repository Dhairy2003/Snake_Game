from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 276)
        self.color("white")
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def score_inc(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
