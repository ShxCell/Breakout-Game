from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("White")
        self.goto(0, 270)
        self.update_scoreboard()
        self.fillcolor("white")

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()

class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.h_score = 0
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.goto(-300, 270)
        self.fillcolor("white")
        self.update_highscore()

    def update_highscore(self):
        self.write(f"High score: {self.h_score}", align=ALIGNMENT, font=FONT)

    def increase_high_score(self, score):
        if score > self.h_score:
            self.h_score = score
            self.clear()
            self.update_highscore()
