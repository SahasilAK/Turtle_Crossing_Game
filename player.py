from turtle import Turtle

#Game Constants

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
	def __init__(self):

		super().__init__()

		self.shape("turtle")
		self.penup()
		self.setheading(90)

		self.goto_start()



	# def move(self):
		
	# 	new_y = self.ycor() + MOVE_DISTANCE
	# 	self.goto(self.xcor(),new_y)

	def move_up(self):

		
		self.forward(MOVE_DISTANCE)


	def is_at_finish_line(self):

		if self.ycor() >FINISH_LINE_Y:
			return True
		else:
			return False

	def goto_start(self):
		self.goto(STARTING_POSITION)
