import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars



#Constants

SPEED = 0.1

#screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

# Player class

player = Player()

#Scoreboard class
score = Scoreboard()

# Car_manger class

cars = Cars()

# Game MOvement Keys

screen.listen()
# screen.onkey(player.move,"w")
screen.onkey(player.move_up,"w")

#Running the game section

game_is_on = True

while game_is_on:
	time.sleep(SPEED)
	screen.update()

	cars.create_cars()
	cars.move_cars()

	# Collison detection

	for car in cars.all_cars:
		if car.distance(player) < 36.5:
			game_is_on = False
			score.game_over()

	if player.is_at_finish_line():
		player.goto_start()
		cars.level_up()
		score.increase_level()




screen.exitonclick()