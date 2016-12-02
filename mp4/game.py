from ball import *
from paddle import *
from qlearning import *
import math


class game(object):
	""" game class """
	def __init__(self):
		self.ball = ball()
		self.paddle = paddle('hardcode')
		self.score = 0
		self.state = (self.ball.x, self.ball.y, self.ball.v_x, self.ball.v_y, self.paddle.y)
		self.termination = False

	def terminate(self):
		self.score -= 1
		self.termination = True

	def check(self):
		if self.ball.x > self.paddle.x:
			if self.ball.y > self.paddle.y and self.ball.y < self.paddle.y + self.paddle.height:
				self.ball.hit()
				self.score += 1
			else:
				self.terminate()

	def updateState(self):
		if self.termination:
			self.state = (12,12,12,12,12)
		else:
			if self.ball.v_x > 0:
				x_velocity = 1
			else:
				x_velocity = -1
			if self.ball.v_y >= 0.015:
				y_velocity = 1
			elif self.ball.v_y <= 0.015:
				y_velocity = -1
			else:
				y_velocity = 0
			discrete_ball_x = min(11, int(math.floor(12 * self.ball.x)))
			discrete_ball_y = min(11, int(math.floor(12 * self.ball.y)))
			discrete_paddle = min(11, int(math.floor(12 * self.paddle.y / (1 - self.paddle.height))))
			self.state = (discrete_ball_x, discrete_ball_y, x_velocity, y_velocity, discrete_paddle)

	def update(self):
		self.ball.update()
		self.paddle.update(self.ball.y)
		self.check()
		self.updateState()
		print self.state
		



