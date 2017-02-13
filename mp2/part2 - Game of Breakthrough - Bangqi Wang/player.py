import numpy as np

from board import board

class player(object):
	def __init__(self, strategy, style, depth):
		# print '__init__ player'
		# 0 - minimax, 1 - alphabeta
		self.strategy = strategy
		# 0 - defensive, 1 - offensive
		self.style = style
		self.depth = depth
		self.node = 0


	def move(self, board, worker):
		# print 'next_move'
		# if the strategy is minimax
		if self.strategy is 0:
			# print 'minimax'
			# depth: 0
			# order: 0 - enemy, 1 - self 
			# worker: 1 - player1, 2 - player2
			node = 0
			best_state = self.minimax(board, 0, 1, worker)
			return best_state[1].step[0]
		# if the strategy is alphabeta
		else:
			# print 'alphabeta'
			# depth: 0
			# order: 0 - enemy, 1 - self 
			# worker: 1 - player1, 2 - player2
			node = 0
			best_state = self.alphabeta(board, 0, 1, worker)
			return best_state[1].step[0]

			
	def minimax(self, board, depth, order, worker):
		self.node += 1
		# if the node is leaf, return evaluation and node
		if depth is self.depth:
			if self.style is 0:
				return (self.heuristic_defensive(board, order, worker), board)
			else:
				return (self.heuristic_offensive(board, order, worker), board)

		# find all possible next step
		queue = []
		next_boards = board.get_next(worker)

		# explore the value of each possible step
		for each_board in next_boards:
			queue.append(self.minimax(each_board, depth+1, 1-order, 3-worker))
		queue = sorted(queue)

		# return max if player is self
		if order is 1:
			return queue[-1]
		# return min if player is enemy
		else:
			return queue[0]


	def alphabeta(self, board, depth, order, worker):
		# return max if player is self
		if order is 1:
			# print 'call max'
			return self.max_value(board, -np.inf, np.inf, depth, order, worker)
		# return min if player is enemy
		else:
			# print 'call min'
			return self.min_value(board, -np.inf, np.inf, depth, order, worker)	

	def min_value(self, board, a, b, depth, order, worker):
		# print 'min_value'
		self.node += 1
		if depth is self.depth:
			# print 'leaf'
			if self.style is 0:
				return (self.heuristic_defensive(board, order, worker), board)
			else:
				return (self.heuristic_offensive(board, order, worker), board)

		v = np.inf
		v_board = None
		# find all possible next step
		queue = []
		next_boards = board.get_next(worker)
		# for i in next_boards:
			# print 'next_boards'
			# print i.state

		for each_board in next_boards:
			each_value = self.max_value(each_board, a, b, depth+1, 1-order, 3-worker)
			if each_value is not None and each_value[0] < v:
				v = each_value[0]
				v_board = each_value
			if v <= a:
				return v_board
			b = min(b, v)
		return v_board

	def max_value(self, board, a, b, depth, order, worker):
		# print 'max_value'
		self.node += 1
		if depth is self.depth:
			# print 'leaf'
			if self.style is 0:
				return (self.heuristic_defensive(board, order, worker), board)
			else:
				return (self.heuristic_offensive(board, order, worker), board)

		v = -np.inf
		v_board = None
		# find all possible next step
		queue = []
		next_boards = board.get_next(worker)
		# for i in next_boards:
			# print 'next_boards'
			# print i.state

		for each_board in next_boards:
			each_value = self.min_value(each_board, a, b, depth+1, 1-order, 3-worker)
			if  each_value is not None and each_value[0] > v:
				v = each_value[0]
				v_board = each_value
			if v >= b:
				return v_board
			a = max(a, v)
		return v_board


	def heuristic_offensive(self, board, order, worker):
		# print 'heuristic_offensive'
		if order is 1:
			# print 'self'
			# print worker
			# print board.get_eval(worker)
			# return board.get_eval(worker)
			return board.get_eval_comb(worker)
		else:
			# print 'enemy'
			# print 3-worker
			# print board.get_eval(3-worker)
			# return board.get_eval(3-worker)
			return board.get_eval_comb(3-worker)


	def heuristic_defensive(self, board, order, worker):
		# print 'heuristic_defensive'
		if order is 1:
			# print 'self'
			# print 3-worker
			# print -1*board.get_eval(3-worker)
			# return -1*board.get_eval(3-worker)
			# return board.get_eval_def(worker)
			return -1*board.get_eval_comb(3-worker)
		else:
			# print 'enemy'
			# print worker
			# print -1*board.get_eval(worker)
			# return -1*board.get_eval(worker)
			# return board.get_eval_def(3-worker)
			return -1*board.get_eval_comb(worker)

	def empty_node(self):
		self.node = 0

