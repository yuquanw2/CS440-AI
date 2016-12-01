

class game(object):
	"""
	game class
	"""
	def __init__(self):
		self.paddle_height = 0.2
		self.state = (0.5, 0.5, 0.03, 0.01, 0.5-self.paddle_height/2)
