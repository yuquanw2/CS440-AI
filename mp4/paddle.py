import random
from ball import *


class paddle(object):
	""" paddle class """
	def __init__(self, agent):
		self.height = 0.2
		self.x = 1.0
		self.y = 0.5 - self.height/2
		self.v = 0.04
		self.agent = agent

	def check(self):
		self.y = max(0, self.y)
		self.y = min(1-self.height, self.y)

	def random(self):
		actions = [0.0, -0.04, 0.04]
		move = random.choice(actions)
		self.y += move
		self.check()

	def hardcode(self, ball_y):
		if ball_y < self.y + self.height/2:
			self.y -= 0.02
		elif ball_y > self.y + self.height/2:
			self.y += 0.02
		self.check()

	def qlearn(self, action):
		self.y += action*0.04
		self.check()

	def update(self, ball_y):
		if self.agent == 'qlearning':
			self.qlearn(ball_y)
		elif self.agent == 'hardcode':
			self.hardcode(ball_y)
		else:
			self.random()