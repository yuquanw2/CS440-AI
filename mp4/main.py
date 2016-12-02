import pygame, sys
from pygame.locals import *
from game import *
import atexit

# Source for drawing
# http://trevorappleton.blogspot.com/2014/04/writing-pong-using-python-and-pygame.html

# number of frames per second
FPS = 200

# window size
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
# line information
LINETHICKNESS = 10
PADDLESIZE = 100
# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

def drawArena():
	DISPLAYSURF.fill(WHITE)

def drawBall(ball, game):
	ball.x = scaleBall(game.ball.x)
	ball.y = scaleBall(game.ball.y)
	pygame.draw.rect(DISPLAYSURF, RED, ball)

def drawPaddle(paddle, game):
	paddle.y = scaleBall(game.paddle.y)
	pygame.draw.rect(DISPLAYSURF, BLACK, paddle)

def drawWall(wall):
	pygame.draw.rect(DISPLAYSURF, BLACK, wall)

def scaleBall(unit):
	return 500*unit - LINETHICKNESS/2

def scalePaddle(unit):
	return 500*unit - LINETHICKNESS

def scaleWall(unit):
	return 500*unit

if __name__=='__main__':
	# initial pygame and surface
	pygame.init()
	global DISPLAYSURF
	
	# set up screen
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
	pygame.display.set_caption('CS440AI_MP4 - Pong Game - Bangqi Wang')
	
	# initialize game
	game = pong()
	# ball
	ball_x = scaleBall(game.state[0])
	ball_y = scaleBall(game.state[1])
	ball = pygame.Rect(ball_x, ball_y, LINETHICKNESS, LINETHICKNESS)
	# paddle
	paddle_x = scalePaddle(1.0)
	paddle_y = scalePaddle(game.state[4])
	paddle_height = scaleWall(game.paddle.height)
	paddle = pygame.Rect(paddle_x, paddle_y, LINETHICKNESS, paddle_height)
	# wall
	wall_x = scaleWall(0.0)
	wall_y = scaleWall(0.0)
	wall = pygame.Rect(wall_x, wall_y, LINETHICKNESS, WINDOWHEIGHT)

	# draw game
	drawArena()
	drawBall(ball, game)
	drawPaddle(paddle, game)
	drawWall(wall)

	while True: # main game loop
		for event in pygame.event.get():
			# exit game
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		# update game
		game.update()
		# if game.termination:
		# 	print game.success
		# 	print game.lose
		# 	game = pong()
		drawArena()
		drawBall(ball, game)
		drawWall(wall)
		drawPaddle(paddle, game)

		# update the screen
		pygame.display.update()
		FPSCLOCK.tick(FPS)


