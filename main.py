import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard, Scoreboard_Timer

level = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard_timer = Scoreboard_Timer()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_backwards, key="Down")
screen.onkey(fun=player.strafe_left, key="Left")
screen.onkey(fun=player.strafe_right, key="Right")

game_is_on = True
LoopCounter = 0
while game_is_on:
    LoopCounter += 1
    time.sleep(0.1)
    screen.update()
    # Move cars under manager purview
    car_manager.move_cars(level)
    # Add additional cars
    if LoopCounter % 40 == 0:
        car_manager.add_cars()
    # Increment Scoreboard Timer
    scoreboard_timer.increment_time()
    # Check for collision
    if car_manager.detect_collision(player_location=player.location):
        # Game Over
        screen.update()
        game_is_on = False
        scoreboard.game_over()
    # # Check to see whether player has won
    if player.level_complete():
        # Increment Level
        level += 1
        scoreboard.increment_level()
        scoreboard_timer.reset_timer()
        # Reset Game
        car_manager.clear_cars()
        car_manager.add_cars()
        player.reset_game()


screen.exitonclick()    # Click to exit game

