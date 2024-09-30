#BASIC RULES
#Breakout begins with eight rows of bricks, with two rows each of a different color.
# The color order from the bottom up is yellow, green, orange and red.
# Using a single ball, the player must knock down as many bricks as possible by using the walls
# and/or the paddle below to hit the ball against the bricks and eliminate them.
# If the player's paddle misses the ball's rebound, they will lose a turn.
# The player has three turns to try to clear two screens of bricks.
# Yellow bricks earn one point each, green bricks earn three points, orange bricks earn five
# points and the top-level red bricks score seven points each. The paddle shrinks to one-half
# its size after the ball has broken through the red row and hit the upper wall.
# Ball speed increases at specific intervals: after twelve hits,
# and after making first contact with the orange and red rows.

#Comment to my solution:
#I have chosen some kids friendly solution which is possible to easily win.
#used OOP, ball controls its movement, paddle controls its movement, score controls lives and hits, bricks have some own properties and main.py controls the game logic
#I have tried to figure out how to create the game on my own, as that was the point of this assignment (NOT to replicated some existing tutorial)

from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from brick import setup_bricks
import time

def scored(ball,nearest_brick, score_board):
    score_board.add_points(nearest_brick.value)

    if nearest_brick.color()[0] == "orange":
        score_board.orange_brick_hit = True
        ball.speed_up()
        screen.tracer(1, delay=ball.delay)


    if nearest_brick.color()[0] == "red":
        score_board.red_brick_hit = True
        ball.speed_up()
        screen.tracer(1, delay=ball.delay)

    bricks.remove(nearest_brick)
    nearest_brick.disappear()
    update_screen(score_board.score, score_board.lives)

    if score_board.hits % 12 == 0:
        ball.speed_up()
        screen.tracer(1, delay=ball.delay)




def update_screen(points, lives):
    screen.title(f"Breakout game       SCORE:    {points}      LIVES:    {lives}")


#setup board
screen = Screen()
screen.bgcolor("black")
screen.title("Breakout game       SCORE:    0      LIVES:    3")
screen.setup(700,600)
screen.tracer(0)

ball = Ball()
score_board = ScoreBoard()
paddle = Paddle((0,-280))
bricks = setup_bricks()

screen.tracer(1, ball.delay)



screen.listen()
screen.onkey(paddle.left,"Left")
screen.onkey(paddle.right,"Right")



game_is_on = True
level = 1
level_distance = 249
won = False


while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.01)


    #Colision with the wall
    if ball.ycor() > 280:
        ball.bounce_y()
        if not score_board.first_top_hit:
            score_board.first_top_hit = True
            level_distance = 124
            paddle.shapesize(stretch_len=12)

    if ball.xcor() < -340 or ball.xcor() > 340:
        ball.bounce_x()

    #Colision with paddle or missed ball
    if won:
        if ball.ycor() < -258:
            ball.bounce_y()
    else:
        if ball.ycor() < -260 and ball.distance(paddle) < level_distance:
            ball.bounce_y()
            #print(ball.distance(paddle))

        if ball.ycor() < -280:
            if score_board.lives >= 1:
                ball.missed()
                score_board.remove_life()
                update_screen(score_board.score, score_board.lives)
                time.sleep(1)


            if score_board.lives == 0:
                screen.title("GAME OVER")
                game_is_on = False

    #Colision with brick

    #find the nearest, if there is no brick reset them
    if len(bricks) == 0 and level == 1:
        ball.reset_position()
        screen.tracer(0)
        bricks = setup_bricks()
        screen.tracer(1,ball.delay)
        level = 2
        score_board.orange_brick_hit = False
        score_board.red_brick_hit = False


    elif len(bricks) == 0 and level == 2:
        screen.title(f"!You won the game! Your score is {score_board.score} points with {score_board.lives} lives")
        #leaving the ball bouncing

        won = True
    else:

        nearest_brick = bricks[0]
        for brick in bricks[1:]:
            if ball.distance(brick) < ball.distance(nearest_brick):
                nearest_brick = brick

        #ball hits the nearest brick
        if ball.distance(nearest_brick) < 40:

            #get the x and y difference based on coordinates to be able bounce the ball in the right direction
            x_difference = ball.xcor() - nearest_brick.xcor()
            y_difference = ball.ycor() - nearest_brick.ycor()

            #if the ball hits the corner of the brick two directions should be bounced
            if abs(y_difference)*2 == abs(x_difference):
                hit_corner = True
            else:
                hit_corner = False

            #bouncing in edge corners
            if hit_corner:
                ball.bounce_y()
                ball.bounce_x()

                scored(ball, nearest_brick, score_board)

            else:

            #bouncing on a single brick edge
                if abs(y_difference)*2 < abs(x_difference):

                    #the ball is on the left if ball xcor is less than brick xcor, x is bounced
                    if ball.xcor() <= nearest_brick.xcor():
                        ball.bounce_x()

                    # the ball is on the right if ball xcor is higher than brick xcor, x is bounced
                    if ball.xcor() >= nearest_brick.xcor():
                        ball.bounce_x()

                    scored(ball, nearest_brick, score_board)

                else:

                    # the ball is on the top if ball ycor is higher than brick ycor,  y is bounced
                    if ball.ycor() <= nearest_brick.ycor():
                        ball.bounce_y()

                    # the ball is on the bottom if ball ycor is less than brick ycor,  y is bounced
                    if ball.ycor() >= nearest_brick.ycor():
                        ball.bounce_y()

                    scored(ball, nearest_brick, score_board)



screen.exitonclick()