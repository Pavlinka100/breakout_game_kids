from turtle import Turtle

class Brick(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("black")
        self.speed(0)
        self.value = 0


    def appear(self, x, y, color,value):
        self.color(color)
        self.goto(x, y)
        self.value = value



    def disappear(self):
        self.hideturtle()





def setup_bricks():
    bricks = []
    y_start = 280

    for color, value in [("red",7), ("orange",5), ("green",3), ("yellow",1)]:
        x_start = -330
        for i in range(14):
            brick_up = Brick()
            brick_up.appear(x_start, y_start, color, value)

            brick_down = Brick()
            brick_down.appear(x_start, y_start - 25, color, value)

            bricks.append(brick_up)
            bricks.append(brick_down)

            x_start += 50
        y_start -= 60

    return bricks


