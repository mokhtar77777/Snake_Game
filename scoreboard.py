from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def read_high_score(self):
        with open("High Score.txt") as file:
            high_score = int(file.read())
            return high_score

    def write_high_score(self, score):
        with open("High Score.txt", mode="w") as file:
            file.write(str(score))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score:  {self.score} High score {self.high_score}", align='center', font=("Courier", 15, "bold"))

    # def print_score_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!!", align='center', font=("Courier", 25, "italic"))

    def high_score_trigger(self):
        if self.score > self.read_high_score():
            self.write_high_score(self.score)
            self.high_score = self.read_high_score()
        self.score = -1
        self.update_score()
