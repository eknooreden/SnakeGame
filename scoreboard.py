from turtle import Turtle
ALIGNMENT = "center"
FONT = ("luckiest guy", 24, "normal")

DATA_FILE_PATH = "/Users/eknoorsingheden/Documents/data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(DATA_FILE_PATH) as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE_PATH, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)        


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()   
