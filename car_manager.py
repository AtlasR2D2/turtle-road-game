from turtle import Turtle
import random
from intersect import Intersect


INITIAL_SHAPE_SIZE = 20
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_LINE_Y = -280
FINISH_LINE_Y = 280
BOTTOM_OF_SCOREBOARD_Y = 250
WEST_HEADING = 180
START_OF_ROAD = 300
END_OF_ROAD = -300


class CarManager:
    def __init__(self):
        self.cars = {}   # Dictionary to hold cars
        self.next_ord = 0
        self.add_cars()

    def add_cars(self):
        random.seed()
        random_car_count = random.randint(0, 10)
        # random_car_count = 1 # For testing
        for i in range(random_car_count):
            self.cars[self.next_ord] = Car()
            self.next_ord += 1

    def clear_cars(self):
        for key in self.cars:
            car_x = self.cars[key]
            car_x.take_off_road()
        self.cars = {}
        self.next_ord = 0

    def move_cars(self, level_x):
        """move all cars in under manager purview"""
        blnRemoveCars = False
        # keys to delete
        listKeysDEL = []
        for key in self.cars:
            car_x = self.cars[key]
            car_x.strafe_left(level=level_x)
            if car_x.xcor() < END_OF_ROAD:
                # Take car off the road
                listKeysDEL.append(key)
        if blnRemoveCars:
            for i in range(len(listKeysDEL)):
                car_x = self.cars[listKeysDEL[i]]
                car_x.take_off_road()
                del self.cars[listKeysDEL[i]]

    def detect_collision(self, player_location):
        """identify if turtle has is within any car location"""
        blnCollision = False
        for key in self.cars:
            car_x = self.cars[key]
            if Intersect(player_location, car_x.location):
                blnCollision = True
                break
        return blnCollision


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.build_car()
        self.car_front = 0
        self.position_car()

    def take_off_road(self):
        self.hideturtle()

    def Identify_Car(self):
        self.color("black")

    def position_car(self):
        random.seed()
        random_y = random.randint(START_LINE_Y, BOTTOM_OF_SCOREBOARD_Y)
        self.goto(x=START_OF_ROAD, y=random_y)
        self.setheading(WEST_HEADING)
        self.set_location()

    def build_car(self):
        random.seed()
        random_color = random.choice(COLORS)
        self.color(random_color)
        self.shape("square")
        self.shapesize(stretch_len=2)

    def set_location(self):
        """contains a nested list of the car location bumper to bumper, door to door"""
        self.car_front = self.xcor() - (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.car_rear = self.xcor() + (self.shapesize()[1] * INITIAL_SHAPE_SIZE / 2)
        self.car_left = self.ycor() - (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.car_right = self.ycor() + (self.shapesize()[0] * INITIAL_SHAPE_SIZE / 2)
        self.location = [(self.car_front, self.car_rear), (self.car_left, self.car_right)]

    def strafe_left(self, level):
        net_move_increment = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
        random_multiplier = random.random()
        net_move_increment *= random_multiplier
        self.goto(x=self.xcor() - net_move_increment, y=self.ycor())
        self.set_location()

