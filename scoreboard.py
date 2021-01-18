from turtle import Turtle




# scoreboard constants
FONT = ("Courier", 15, "normal")
SCORE_ALIGN = "center"
SCORE_LOC = (-230, 260)


class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()

		self.level = 0
		self.penup()
		self.hideturtle()

		self.update_scoreboard()

	def update_scoreboard(self):
		self.goto(SCORE_LOC)
		self.write(f'Level : {self.level}',False , SCORE_ALIGN,FONT)

	def increase_level(self):
		self.level += 1
		self.clear()
		self.update_scoreboard()

	def game_over(self):
		self.goto(0,0)
		self.write(f'Game Over',False , SCORE_ALIGN,FONT)
		self.goto(0,-40)
		self.write(f'You Reached Level : {self.level}',False , SCORE_ALIGN,FONT)








		
