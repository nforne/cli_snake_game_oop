from turtle import Turtle


class Scoreboard(Turtle):
    ALIGNMENT = 'center'
    FONT = ('Ariel', 24, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=self.ALIGNMENT, font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
