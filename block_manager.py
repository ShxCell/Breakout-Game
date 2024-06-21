from turtle import Turtle
import random


class Block(Turtle):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=width, stretch_wid=height)
        self.penup()
        self.goto(x=x, y=y)
        self.active = True

    def hide(self):
        self.goto(1000, 2000)
        self.active = False


def generate_block(blocks):
    blocks = blocks
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "violet"]
    y_start = 250

    for i in range(8):
        for j in range(-350, 351, 70):
            block = Block(j, y_start - (i * 30), 3, 1, colors[i])
            blocks.append(block)


def is_collision(ball, block):
    if (block.active and
            block.xcor() + 30 > ball.xcor() > block.xcor() - 30 and
            block.ycor() + 30 > ball.ycor() > block.ycor() - 30):
        return True
    else:
        return False
