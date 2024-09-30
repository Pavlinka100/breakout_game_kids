from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=25)
        self.goto(position)
        self.color("white")
        self.score = 0
        self.speed = 0



    def right(self):
        if self.xcor() < 260:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def left(self):
        if self.xcor() > -260:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

