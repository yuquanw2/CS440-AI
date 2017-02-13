from ball import *
from paddle import *
from qlearning import *
import math


ALPHA = 50
GAMMA = 0.7
EPSILON = 0.05
ROUND = 200000
LIMIT = True
OPTIMAL = False


class pongtwo(object):
	""" game pongtwo """
	def __init__(self):
		self.ball = ball()
		self.paddle1 = paddle('qlearning')
		self.paddle2 = paddle('hardcode')
		self.qlearning = qlearning(epsilon=EPSILON, alpha=ALPHA, gamma=GAMMA)
		self.state = (self.ball.x, self.ball.y, self.ball.v_x, self.ball.v_y, self.paddle1.y)
		self.lastState = None
		self.lastAction = None
		self.success = 0
		self.winrate = [0]
		self.score = 0
		self.lose = 0
		self.hit = False
		self.scores = []
		self.round = 0
		self.termination = False
		self.termination2 = False
		self.finish = False
		self.x = [0]
		self.y = [0]

	def loadWeight(self):
		with open('weight.txt', 'r') as weightFile:
			for line in weightFile:
				line = line.strip().split(' ')
				state = (int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]))
				action = int(line[5])
				weight = float(line[6])
				self.qlearning.q[(state, action)] = weight

	def terminate(self):
		if len(self.scores) == 1000:
			self.scores = self.scores[1:]
		self.scores.append(self.score)
		self.score = 0
		self.round += 1
		total = 0
		if self.round%1000 == 0:
			total = float(sum(self.scores))/1000.0
			self.x.append(self.round)
			self.y.append(total)
			winning = float(self.success) / float(self.success + self.lose)
			self.winrate.append(10.0*winning)
			print self.round
			print total
			print winning
		if LIMIT:
			if self.round == ROUND:
				self.finish = True
		if OPTIMAL:
			if total > 9.0:
				self.finish = True

	def check(self):
		if self.ball.x > self.paddle1.x:
			if self.ball.y > self.paddle1.y and self.ball.y < self.paddle1.y + self.paddle1.height:
				self.ball.hit()
				self.score += 1
				self.hit = True
			else:
				self.terminate()
				self.termination = True
				self.lose += 1
		if self.ball.x < self.paddle2.x:
			if self.ball.y > self.paddle2.y and self.ball.y < self.paddle2.y + self.paddle2.height:
				# print 'hit'
				self.ball.hit2()
				self.score += 1
			else:
				self.termination2 = True
				self.terminate()
				self.success += 1

	def updateState(self):
		if self.termination:
			return (12,12,12,12,12)
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
			discrete_paddle1 = min(11, int(math.floor(12 * self.paddle1.y / (1 - self.paddle1.height))))
			return (discrete_ball_x, discrete_ball_y, x_velocity, y_velocity, discrete_paddle1)

	def update(self):
		self.check()
		state = self.updateState()
		reward = 0.0

		if self.termination:
			reward = -1000.0
			if self.lastState is not None:
				self.qlearning.learn(self.lastState, self.lastAction, reward, state)
			self.lastState = None
			# restart game
			self.ball = ball()
			self.paddle1 = paddle('qlearning')
			self.paddle2 = paddle('hardcode')
			self.termination = False
			return
		if self.termination2:
			reward = 1000.0
			if self.lastState is not None:
				self.qlearning.learn(self.lastState, self.lastAction, reward, state)
			self.lastState = None
			# restart game
			self.ball = ball()
			self.paddle1 = paddle('qlearning')
			self.paddle2 = paddle('hardcode')
			self.termination2 = False
			return
		if self.hit:
			self.hit = False
			reward = 100.0
		if self.lastState is not None:
			self.qlearning.learn(self.lastState, self.lastAction, reward, state)

		state = self.updateState()
		action = self.qlearning.chooseAction(state)
		# action = self.qlearning.chooseActionRandom()
		self.lastState = state
		self.lastAction = action
		self.paddle1.update(action)
		self.paddle2.update(self.ball.y)
		self.ball.update()
		



