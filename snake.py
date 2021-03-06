from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.x_cor = 0
        self.segments = []
        self.create_snake()

    def create_snake(self):
        self.x_cor = 0
        for turtle in range(3):
            new_turtle = Turtle()
            self.turtle_setup(new_turtle)
            new_turtle.setx(self.x_cor)
            self.segments.append(new_turtle)
            self.x_cor -= 20
        self.segments[0].color("yellowgreen")

    def turtle_setup(self, turtle):
        turtle.shape("square")
        turtle.penup()
        turtle.color("white")

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            position_of_prev = self.segments[seg_number - 1].position()
            self.segments[seg_number].goto(position_of_prev)
        self.segments[0].forward(20)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def up(self):
        # print(str(self.segments[0].xcor()) + " " + str(self.segments[1].xcor()))
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def increase_length(self, position_of_last):
        new_turtle = Turtle()
        self.turtle_setup(new_turtle)
        new_turtle.goto(position_of_last)
        self.segments.append(new_turtle)

    def add_new_segment(self):
        position_of_last = self.segments[-1].position()
        self.increase_length(position_of_last)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
