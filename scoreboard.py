from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initial Level
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-200, y=250)
        self.show_level()

    def increment_level(self):
        self.level += 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)


class Scoreboard_Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=200, y=250)
        self.reset_timer()

    def increment_time(self):
        self.time_elapsed = time.time() - self.timestart
        self.show_timer()

    def print_time_to_console(self, level_x):
        print(f"Level {level_x}: Time elapsed {self.strTimer}")

    def reset_timer(self):
        self.timestart = time.time()
        self.time_elapsed = self.timestart - self.timestart
        self.show_timer()

    def show_timer(self):
        self.clear()
        self.strTimer = str(round(self.time_elapsed,2))+"s"
        self.write(arg=self.strTimer, align=ALIGNMENT, font=FONT)
