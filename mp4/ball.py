class ball(object):
	""" ball class """
	def __init__(self):
		self.x = 0.5
		self.y = 0.5
		self.v_x = 0.03
		self.v_y = 0.01

	def rebound(self):
		pass

	def lose(self):
		pass

	def check(self):
		pass

	def update(self):
		self.x += self.v_x
		self.y += self.v_y
		