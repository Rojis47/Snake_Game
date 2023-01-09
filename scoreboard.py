from turtle import Turtle

end = Turtle()
score_board = Turtle()
score = Turtle()

class TrackOfScore(Turtle):
    player_score = 0

    def __init__(self):
        super().__init__()
        score_board.color("white")
        score_board.hideturtle()
        score_board.penup()
        score_board.goto(0, 260)
        score_board.write(arg=f"score: {self.player_score} ", move=False, align="center", font=('Courier', 17, 'normal'))


    def update_score(self):
        self.player_score += 1
        score_board.clear()
        score_board.write(arg=f"score: {self.player_score} ", move=False, align="center", font=('Courier', 17, 'normal'))


    def game_over(self):
        end.color("white")
        end.hideturtle()
        end.penup()
        end.goto(0,0)
        end.write("GAME OVER", align="center", font=("Courier", 17, "normal"))
