from ball import *
from paddle import *


class game(object):
	""" game class """
	def __init__(self):
		self.ball = ball()
		self.paddle = paddle()
		self.score = 0
		self.state = (self.ball.x, self.ball.y, self.ball.v_x, self.ball.v_y, self.paddle.y)

	def update(self):
		self.paddle.update()
		self.ball.update()
		self.state = (self.ball.x, self.ball.y, self.ball.v_x, self.ball.v_y, self.paddle.y)
		



