import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard, HighScore
from block_manager import Block, generate_block, is_collision

screen = Screen()
screen.tracer(0)
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My Pong game")

# Create a paddle
paddle = Paddle((0, -270))

# Create ball
ball = Ball()

# Create blocks
blocks = []
generate_block(blocks)


# create score
scoreboard = Scoreboard()
highscore = HighScore()

# Make paddle move
screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the wall
    if ball.xcor() < -375 or ball.xcor() > 375:
        # bounce x
        ball.bounce_x()
    elif ball.ycor() > 275:
        # bounce y
        ball.bounce_y()

    # when paddle miss
    if ball.ycor() < -310:
        ball.reset_position()
        highscore.increase_high_score(scoreboard.score)
        scoreboard.reset_score()

    # detect collision with paddle
    if ball.ycor() < -240 and ball.distance(paddle) < 50:
        print("made contact")
        ball.bounce_y()

    # detect collision with block
    for block in blocks:
        if is_collision(ball, block):
            ball.bounce_y()
            block.hide()
            scoreboard.increase_score()

screen.exitonclick()
