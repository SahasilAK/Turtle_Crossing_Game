from turtle import Turtle




# scoreboard constants
FONT = ("Courier", 12, "normal")
SCORE_ALIGN = "center"
SCORE_LOC = (-230, 260)
HSCORE_LOC = (-220, 240)


class Scoreboard(Turtle):
	
	def __init__(self):
		super().__init__()

		self.level = 0
		self.penup()
		self.hideturtle()
		with open("data.txt") as data:
			self.high_score = int(data.read())

		self.update_scoreboard()

	def update_scoreboard(self):
		self.goto(SCORE_LOC)
		self.write(f'Level : {self.level}',False , SCORE_ALIGN,FONT)

		self.goto(HSCORE_LOC)
		self.write(f'High Score : {self.high_score}',False , SCORE_ALIGN,FONT)

	def increase_level(self):
		self.level += 1
		self.clear()
		self.update_scoreboard()


	def game_over(self):
		self.goto(0,0)
		self.write(f'Game Over',False , SCORE_ALIGN,FONT)
		self.goto(0,-40)
		self.write(f'You Reached Level : {self.level}',False , SCORE_ALIGN,FONT)
		if self.level > self.high_score:
			self.high_score = self.level

			hscore = str(self.high_score)
			with open("data.txt",mode = "w") as data:

				data.write(hscore)









		
