import numpy as np
from player import player
from board import board
from time import time

class game:
	def __init__(self, strategy_player1, style_player1, strategy_player2, style_player2):
		# print '__init__ game'
		# initialize the board and players
		self.board = board()
		self.player1 = player(strategy_player1, style_player1, 5)
		self.player2 = player(strategy_player2, style_player2, 5)
		# 1 - player1, 2 - player2
		self.turn = 1
		# True - finished, False - running
		self.finish = False
		# 0 - no winner, 1 - player1, 2 - player2
		self.winner = ''
		self.step = 0
		self.step1 = 0
		self.step2 = 0
		self.node = 0
		self.time1 = 0
		self.time2 = 0
		self.str1 = ''
		self.str2 = ''
		self.sty1 = ''
		self.sty2 = '' 
		if strategy_player1 == 0:
			self.str1 = 'MiniMax'
		else:
			self.str1 = 'AlphaBeta'
		if strategy_player2 == 0:
			self.str2 = 'MiniMax'
		else:
			self.str2 = 'AlphaBeta'

		if style_player1 == 0:
			self.sty1 = 'Defensive'
		else:
			self.sty1 = 'Offensive'

		if style_player2 == 0:
			self.sty2 = 'Defensive'
		else:
			self.sty2 = 'Offensive'



	def check_win(self):
		# print 'check_win'
		if 1 in self.board.state[7]:
			self.finish = True
			self.winner = 'Player_1'
		elif 2 in self.board.state[0]:
			self.finish = True
			self.winner = 'Player_2'
		elif 1 not in self.board.state:
			self.finish = True
			self.winner = 'Player_2'
		elif 2 not in self.board.state:
			self.finish = True
			self.winner = 'Player_1'
		else:
			self.finish = False
			self.winner = 0

	def solve(self):
		# print 'solve'
		while self.finish is False:
		# for i in range(1):
			# print self.turn
			if self.turn is 1:
				print('AI Turn:\n')
				# print 'player1:'
				start = time()
				step = self.player1.move(self.board, 1)
				end = time()
				self.time1 += end - start
				# print self.player1.node
				# self.node += self.player1.node
				# self.player1.empty_node()
				print step
				self.board.set_move(step)
				self.board.empty_step()
				self.step1 += 1
				self.step += 1
				self.turn = 2
				self.check_win()
			else:
				print('\nYour Turn:\n')
				start = time()
				step = self.player2.move(self.board, 2)
				s_x = int(raw_input("Please enter start row [0,8): \n"))
				s_y = int(raw_input("Please enter start column [0,8): \n"))
				if self.board.state[s_x][s_y] != 2:
					print('Wrong Move! Please select your piece.')
					continue
				direction = int(raw_input("Please enter direction [0,3): \n"))
				e_y = 0
				e_x = 0
				if direction == 0:
					e_x = s_x - 1
					e_y = e_y - 1
					if e_y < 0:
						print('Wrong Move! Cannot move left.')
						continue
				elif direction == 1:
					e_x = s_x - 1
					e_y = s_y
				elif direction == 2:
					e_x = s_x - 1
					e_y = s_y + 1
					if e_y > 7:
						print('Wrong Move! Cannot move right.')
						continue
				else:
					print('Wrong Move! Please enter number 0~2.')
				step = ((s_x,s_y),(e_x,e_y))
				if self.board.state[e_x][e_y] == 2:
					print('Wrong Move! Cannot capture your piece.')
					continue
				step = ((s_x,s_y),(e_x,e_y))
				print step
				end = time()
				self.time2 += end - start
				self.board.set_move(step)
				self.board.empty_step()
				self.step2 += 1
				self.step += 1
				self.turn = 1
				self.check_win()
			# else:
			# 	# print 'player2:'
			# 	# print self.board.state
			# 	start = time()
			# 	step = self.player2.move(self.board, 2)
			# 	end = time()
			# 	self.time2 += end - start
			# 	# self.node += self.player2.node
			# 	# print self.player2.node
			# 	# self.player2.empty_node()
			# 	# print step
			# 	self.board.set_move(step)
			# 	self.board.empty_step()
			# 	self.step2 += 1
			# 	self.step += 1
			# 	self.turn = 1
			# 	self.check_win()
			print self.board.state
		print ''
		print self.board.state
		print 'Winner: {}'.format(self.winner)
		print 'Strategy: {} vs. {}'.format(self.str1, self.str2)
		print 'Style: {} vs. {}'.format(self.sty1, self.sty2)
		print 'Depth: {} vs. {}'.format(self.player1.depth, self.player2.depth)
		print 'Node Expanded: {} vs. {}'.format(self.player1.node, self.player2.node)
		print 'Node Exp/Move: {} vs. {}'.format(self.player1.node/self.step1, self.player2.node/self.step2)
		print 'Avg Time/Move: {} vs. {}'.format(round(self.time1/self.step1, 4), round(self.time2/self.step2, 4))
		print 'Oppo Captured: {} vs. {}'.format(self.board.cap1, self.board.cap2)
		print 'moves to Win : {}'.format(self.step)
		print ''




		# print self.step



