import numpy as np
from copy import deepcopy

class board:
	def __init__(self):
		# self.size_x = 5
		# self.size_y = 10
		# self.state = np.array( [[1,1,1,1,1],
		# 						[1,1,1,1,1],
		# 						[0,0,0,0,0],
		# 						[0,0,0,0,0],
		# 						[0,0,0,0,0],
		# 						[0,0,0,0,0],
		# 						[0,0,0,0,0],
		# 						[0,0,0,0,0],
		# 						[2,2,2,2,2],
		# 						[2,2,2,2,2]])
		self.size_x = 8
		self.size_y = 8
		self.state = np.array( [[1,1,1,1,1,1,1,1],
								[1,1,1,1,1,1,1,1],
								[0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0],
								[0,0,0,0,0,0,0,0],
								[2,2,2,2,2,2,2,2],
								[2,2,2,2,2,2,2,2]])
		self.step = []
		self.cap1 = 0
		self.cap2 = 0

	def get_copy(self):
		# print 'board: get_copy'
		return deepcopy(self)

	def set_move(self, move):
		# print 'board: set_move'
		current = move[0]
		next = move[1]
		if self.state[next[0]][next[1]] == 1:
			self.cap2 += 1
		elif self.state[next[0]][next[1]] == 2:
			self.cap1 += 1
		self.state[next[0]][next[1]] = self.state[current[0]][current[1]]
		self.state[current[0]][current[1]] = 0
		self.step.append(move)


	def empty_step(self):
		self.step = []

	def get_next(self, worker):
		# print 'get_next'
		next_boards = []
		if worker == 1:
			for j in range(self.size_y):
				j = self.size_y - 1 - j
				for i in range(self.size_x):
					# i = 7-i
					if self.state[j][i] == 1 and j + 1 < self.size_y:
						if i - 1 >= 0 and self.state[j+1][i-1] != 1:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j+1,i-1)))
							next_boards.append(cur_board)
						if self.state[j+1][i] == 0:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j+1,i)))
							next_boards.append(cur_board)
						if i + 1 < self.size_x and self.state[j+1][i+1] != 1:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j+1,i+1)))
							next_boards.append(cur_board)
						
						

		elif worker == 2:
			for j in range(self.size_y):
				for i in range(self.size_x):
					if self.state[j][i] == 2 and j - 1 >= 0:
						if i - 1 >= 0 and self.state[j-1][i-1] != 2:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j-1,i-1)))
							next_boards.append(cur_board)
						if self.state[j-1][i] == 0:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j-1,i)))
							next_boards.append(cur_board)
						if i + 1 < self.size_x and self.state[j-1][i+1] != 2:
							cur_board = self.get_copy()
							cur_board.set_move(((j,i),(j-1,i+1)))
							next_boards.append(cur_board)
		return next_boards

	def get_eval(self, worker):
		self.distance = 0
		self.capture = 16
		if worker is 1:
			for j in range(self.size_y):
				for i in range(self.size_x):
					if self.state[j][i] == worker:
						self.distance += j*j
						if j == self.size_y - 1:
							self.distance += 1600
					elif self.state[j][i] == 3-worker:
						self.capture -= 1
		if worker is 2:
			for j in range(self.size_y):
				for i in range(self.size_x):
					if self.state[j][i] == worker:
						self.distance += (7-j)*(7-j)
						if j == 0:
							self.distance += 1600
					elif self.state[j][i] == 3-worker:
						self.capture -= 1
		return self.distance + 100*self.capture

	def get_eval_comb(self, worker):
		self.distance = 0
		self.danger = 0
		self.capture = 16
		self.lost = 16
		if worker is 1:
			for j in range(self.size_y):
				for i in range(self.size_x):
					if self.state[j][i] == worker:
						self.distance += j
						self.lost -= 1
						if j == self.size_y - 1:
							self.distance += 800
					elif self.state[j][i] == 3-worker:
						self.capture -= 1
						self.danger += (7-j)
		if worker is 2:
			for j in range(self.size_y):
				for i in range(self.size_x):
					if self.state[j][i] == worker:
						self.distance += (7-j)
						self.lost -= 1
						if j == 0:
							self.distance += 800
					elif self.state[j][i] == 3-worker:
						self.capture -= 1
						self.danger += j
		return (self.distance + self.capture) - (self.danger + self.lost)


	# def get_eval_def(self, worker):
	# 	self.distance = 0
	# 	self.piece = 0
	# 	self.capture = 16
	# 	if worker is 1:
	# 		for j in range(self.size_y):
	# 			for i in range(self.size_x):
	# 				if self.state[j][i] == 3-worker:
	# 					self.distance += j
	# 					self.capture -= 1
	# 					if j == 0:
	# 						self.distance = -1600
	# 					elif self.state[j][i] == worker:
	# 						self.piece += 1
	# 						if j == self.size_y - 1:
	# 							self.distance = 1600
	# 	if worker is 2:
	# 		for j in range(self.size_y):
	# 			for i in range(self.size_x):
	# 				if self.state[j][i] == 3-worker:
	# 					self.distance += (7-j)
	# 					self.capture -= 1
	# 					if j == self.size_y - 1:
	# 						self.distance = -1600
	# 					elif self.state[j][i] == worker:
	# 						self.piece += 1
	# 						if j == 0:
	# 							self.distance = 1600
	# 	return self.distance + 100*self.piece + 50*self.capture

