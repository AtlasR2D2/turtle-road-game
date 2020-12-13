from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH_HEADING = 90
INITIAL_SHAPE_SIZE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.fillcolor("black")
        self.penup()
        self.setheading(NORTH_HEADING)
        self.reset_game()

    def reset_game(self):
        self.goto(STARTING_POSITION)
        self.set_location()

    def move_up(self):
        self.forward(MOVE_DISTANCE)
        self.set_location()

    def move_backwards(self):
        self.back(MOVE_DISTANCE)
        self.set_location()

    def strafe_left(self):
        self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())
        self.set_location()

    def strafe_right(self):
        self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())
        self.set_location()

    def set_location(self):
        """contains a nested list of the car location bumper to bumper, door to door"""
        player_left = self.xcor() - self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2
        player_right = self.xcor() + self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2
        player_rear = self.ycor() - self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2
        player_front = self.ycor() + self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2
        self.location = [(player_left, player_right), (player_rear, player_front)]
    def level_complete(self):
        """Returns True if player reaches finish line """
        return self.ycor() >= FINISH_LINE_Y
