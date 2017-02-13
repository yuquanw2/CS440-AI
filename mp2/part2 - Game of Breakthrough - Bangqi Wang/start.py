from game import game
from board import board
from player import player
from time import time

strategy_player1 = 1
strategy_player2 = 1
style_player1 = 0
style_player2 = 0


game = game(strategy_player1, style_player1, strategy_player2, style_player2)
game.solve()
# board = board()
# array = board.get_next(1)
# print len(array)