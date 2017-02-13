import random


class ball(object):
	""" ball class """
	def __init__(self):
		self.x = 0.5
		self.y = 0.5
		self.v_x = 0.03
		self.v_y = 0.01

	def bounce(self):
		if self.y < 0:
			self.y = -self.y
			self.v_y = -self.v_y
		elif self.y > 1:
			self.y = 2 - self.y
			self.v_y = -self.v_y
		elif self.x < 0:
			self.x = -self.x
			self.v_x = -self.v_x

	def hit(self):
		self.x = 2 - self.x
		U = random.uniform(-0.015, 0.015)
		V = random.uniform(-0.03, 0.03)
		self.v_x = -self.v_x + U
		self.v_y += V
		if self.v_x < 0:
			self.v_x = max(-1.0, min(-0.03, self.v_x))
		elif self.v_x > 0:
			self.v_y = min(1.0, max(0.03, self.v_y))
		if self.v_y < 0:
			self.v_y = max(-1.0, self.v_y)
		elif self.v_y > 0:
			self.v_y = min(1.0, self.v_y)

	def update(self):
		self.x += self.v_x
		self.y += self.v_y
		self.bounce()

		