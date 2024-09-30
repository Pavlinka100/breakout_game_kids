import time
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("yellow")
        self.x_move = 10
        self.y_move = 10
        self.speed(1)
        self.delay = 15




    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        #time.sleep(0.1)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()


    def missed(self):
        self.hideturtle()
        self.reset_position()
        self.showturtle()

    def speed_up(self):
        if self.delay >=2:
            self.delay -=1

