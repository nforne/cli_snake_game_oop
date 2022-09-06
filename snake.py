from turtle import Turtle


class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE_DISTANCE = 20
    UP = 90
    DOWN = -90
    LEFT = 180
    RIGHT = 0

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(self.MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        #    add a new segment to the snake
        self.add_segment(position=self.segments[-1].position())

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
