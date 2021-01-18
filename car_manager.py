from turtle import Turtle
import random

#Car Constants

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREAMENT = 10

# class Cars(Turtle):
	
# 	def __init__(self):
# 		super().__init__()

# 		self.all_cars = []
		


# 	def create_cars(self):
# 		new_car = self.shape("square")
# 		new_car = self.penup()
# 		new_car = self.shapesize(stretch_wid = 1 ,stretch_len = 3)
# 		new_car = self.color(random.choice(COLORS))

# 		random_y = random.randint(-250, 250)

# 		new_car =  self.goto(300, random_y)

# 		self.all_cars.append(new_car)


class Cars():
	def __init__(self):
		

		self.all_cars = []
		self.car_speed = STARTING_MOVE_DISTANCE
		


	def create_cars(self):

		random_chance = random.randint(1,6)
		if random_chance == 1 :
			new_car = Turtle("square")
			new_car.penup()
			new_car.shapesize(stretch_wid = 1 ,stretch_len = 3)
			new_car.color(random.choice(COLORS))

			random_y = random.randint(-250, 250)

			new_car.goto(300, random_y)

			self.all_cars.append(new_car)
		

	def move_cars(self):
		for car in self.all_cars:
			car.backward(self.car_speed)

	def level_up(self):
		self.car_speed += MOVE_INCREAMENT



		




