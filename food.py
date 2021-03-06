from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.generate_new_location()

    def generate_new_location(self):
        x_value = random.randint(-280, 270)
        y_value = random.randint(-280, 270)
        self.goto(x_value, y_value)