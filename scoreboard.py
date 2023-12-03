from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("luckiest guy", 24, "normal"))

    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()   
