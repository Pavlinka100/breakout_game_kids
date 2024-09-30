import time
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.hits = 0
        self.red_brick_hit = False
        self.orange_brick_hit = False
        self.first_top_hit = False


    def add_points(self, points):
        self.score += points
        self.add_hit_count()

    def remove_life(self):
        self.lives -= 1

    def add_hit_count(self):
        self.hits += 1