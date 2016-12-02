import numpy as np
import random

# https://github.com/studywolf/blog/blob/master/RL/Cat%20vs%20Mouse%20exploration/qlearn.py

class qlearning(object):
	""" qlearning """
	def __init__(self, epsilon, alpha, gamma):
		self.epsilon = epsilon
		self.alpha = alpha
		self.gamma = gamma
		self.q = {}
		self.actions = [-1, 0, 1]

	def getQ(self, state, action):
		return self.q.get((state, action), 0.0)
 
 	def learnQ(self, state, action, reward, value):
 		oldv = self.q.get((state, action), None)
 		if oldv is None:
 			self.q[(state, action)] = reward
 		else:
 			self.q[(state, action)] = oldv + self.alpha * (value - oldv)

 	def chooseAction(self, state):
 		if random.random < self.epsilon:
 			action = random.choice(self.actions)
 		else:
 			q = [self.getQ(state, a) for a in self.actions]
 			maxQ = max(q)
 			if q.count(maxQ) > 1:
 				best = [i for i in range(3) if q[i] == maxQ]
 				return self.actions[random.choice(best)]
 			else:
 				return self.actions[q.index(maxQ)]

 	def learn(self, state1, action1, reward, state2):
 		maxqnew = max([self.getQ(state2, a) for a in self.actions])
 		self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)


		