import Queue as Q
from copy import deepcopy
from time import time

queue = Q.PriorityQueue()
def heuristic(cube_h):
	diff = 0
	goal = ['r','r','r','r','b','b','b','b','g','g','g','g','o','o','o','o','y','y','y','y','p','p','p','p']
	for i in range(24):
		if cube_h[i] is not goal[i]:
			diff += 1
	return diff

def rotate_top_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_t = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_t['top'][0]
	cube_t['top'][0] = cube_t['top'][2]
	cube_t['top'][2] = cube_t['top'][3]
	cube_t['top'][3] = cube_t['top'][1]
	cube_t['top'][1] = temp
	
	# change side
	temp1 = cube_t['left'][1]
	temp2 = cube_t['left'][3]
	cube_t['left'][1] = cube_t['front'][0]
	cube_t['left'][3] = cube_t['front'][1]
	cube_t['front'][0] = cube_t['right'][2]
	cube_t['front'][1] = cube_t['right'][0]
	cube_t['right'][2] = cube_t['back'][3]
	cube_t['right'][0] = cube_t['back'][2]
	cube_t['back'][3] = temp1
	cube_t['back'][2] = temp2

	# change path
	cube_t['path'].append('T')
	cube_heu = []
	cube_heu = cube_t['left'] + cube_t['top'] + cube_t['right'] + cube_t['front'] + cube_t['bottom'] + cube_t['back']
	diff = heuristic(cube_heu) + len(cube_t['path'])
	queue.put((diff, cube_t))
	# print(cube_t['path'])

def rotate_top_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_t_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_t_c['top'][0]
	cube_t_c['top'][0] = cube_t_c['top'][1]
	cube_t_c['top'][1] = cube_t_c['top'][3]
	cube_t_c['top'][3] = cube_t_c['top'][2]
	cube_t_c['top'][2] = temp
	
	# change side
	temp1 = cube_t_c['left'][1]
	temp2 = cube_t_c['left'][3]
	cube_t_c['left'][1] = cube_t_c['back'][3]
	cube_t_c['left'][3] = cube_t_c['back'][2]
	cube_t_c['back'][3] = cube_t_c['right'][2]
	cube_t_c['back'][2] = cube_t_c['right'][0]
	cube_t_c['right'][2] = cube_t_c['front'][0]
	cube_t_c['right'][0] = cube_t_c['front'][1]
	cube_t_c['front'][0] = temp1
	cube_t_c['front'][1] = temp2

	# change path
	cube_t_c['path'].append('T\'')
	cube_heu = []
	cube_heu = cube_t_c['left'] + cube_t_c['top'] + cube_t_c['right'] + cube_t_c['front'] + cube_t_c['bottom'] + cube_t_c['back']
	diff = heuristic(cube_heu) + len(cube_t_c['path'])
	queue.put((diff, cube_t_c))
	# print(cube_t_c['path'])

def rotate_front_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_f = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_f['front'][0]
	cube_f['front'][0] = cube_f['front'][2]
	cube_f['front'][2] = cube_f['front'][3]
	cube_f['front'][3] = cube_f['front'][1]
	cube_f['front'][1] = temp
	
	# change side
	temp1 = cube_f['top'][2]
	temp2 = cube_f['top'][3]
	cube_f['top'][2] = cube_f['left'][2]
	cube_f['top'][3] = cube_f['left'][3]
	cube_f['left'][2] = cube_f['bottom'][1]
	cube_f['left'][3] = cube_f['bottom'][0]
	cube_f['bottom'][0] = cube_f['right'][3]
	cube_f['bottom'][1] = cube_f['right'][2]
	cube_f['right'][2] = temp1
	cube_f['right'][3] = temp2

	# change path
	cube_f['path'].append('F')
	cube_heu = []
	cube_heu = cube_f['left'] + cube_f['top'] + cube_f['right'] + cube_f['front'] + cube_f['bottom'] + cube_f['back']
	diff = heuristic(cube_heu) + len(cube_f['path'])
	queue.put((diff, cube_f))
	# print(cube_f['path'])

def rotate_front_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_f_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_f_c['front'][0]
	cube_f_c['front'][0] = cube_f_c['front'][1]
	cube_f_c['front'][1] = cube_f_c['front'][3]
	cube_f_c['front'][3] = cube_f_c['front'][2]
	cube_f_c['front'][2] = temp
	
	# change side
	temp1 = cube_f_c['top'][2]
	temp2 = cube_f_c['top'][3]
	cube_f_c['top'][2] = cube_f_c['right'][2]
	cube_f_c['top'][3] = cube_f_c['right'][3]
	cube_f_c['right'][2] = cube_f_c['bottom'][1]
	cube_f_c['right'][3] = cube_f_c['bottom'][0]
	cube_f_c['bottom'][0] = cube_f_c['left'][3]
	cube_f_c['bottom'][1] = cube_f_c['left'][2]
	cube_f_c['left'][2] = temp1
	cube_f_c['left'][3] = temp2

	# change path
	cube_f_c['path'].append('F\'')
	cube_heu = []
	cube_heu = cube_f_c['left'] + cube_f_c['top'] + cube_f_c['right'] + cube_f_c['front'] + cube_f_c['bottom'] + cube_f_c['back']
	diff = heuristic(cube_heu) + len(cube_f_c['path'])
	queue.put((diff, cube_f_c))
	# print(cube_f_c['path'])

def rotate_bottom_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_bo = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_bo['bottom'][0]
	cube_bo['bottom'][0] = cube_bo['bottom'][2]
	cube_bo['bottom'][2] = cube_bo['bottom'][3]
	cube_bo['bottom'][3] = cube_bo['bottom'][1]
	cube_bo['bottom'][1] = temp
	
	# change side
	temp1 = cube_bo['front'][2]
	temp2 = cube_bo['front'][3]
	cube_bo['front'][2] = cube_bo['left'][0]
	cube_bo['front'][3] = cube_bo['left'][2]
	cube_bo['left'][0] = cube_bo['back'][1]
	cube_bo['left'][2] = cube_bo['back'][0]
	cube_bo['back'][0] = cube_bo['right'][1]
	cube_bo['back'][1] = cube_bo['right'][3]
	cube_bo['right'][1] = temp2
	cube_bo['right'][3] = temp1

	# change path
	cube_bo['path'].append('Bo')
	cube_heu = []
	cube_heu = cube_bo['left'] + cube_bo['top'] + cube_bo['right'] + cube_bo['front'] + cube_bo['bottom'] + cube_bo['back']
	diff = heuristic(cube_heu) + len(cube_bo['path'])
	queue.put((diff, cube_bo))
	# print(cube_bo['path'])


def rotate_bottom_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_bo_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_bo_c['bottom'][0]
	cube_bo_c['bottom'][0] = cube_bo_c['bottom'][1]
	cube_bo_c['bottom'][1] = cube_bo_c['bottom'][3]
	cube_bo_c['bottom'][3] = cube_bo_c['bottom'][2]
	cube_bo_c['bottom'][2] = temp
	
	# change side
	temp1 = cube_bo_c['front'][2]
	temp2 = cube_bo_c['front'][3]
	cube_bo_c['front'][2] = cube_bo_c['right'][3]
	cube_bo_c['front'][3] = cube_bo_c['right'][1]
	cube_bo_c['right'][1] = cube_bo_c['back'][0]
	cube_bo_c['right'][3] = cube_bo_c['back'][1]
	cube_bo_c['back'][0] = cube_bo_c['left'][2]
	cube_bo_c['back'][1] = cube_bo_c['left'][0]
	cube_bo_c['left'][0] = temp1
	cube_bo_c['left'][2] = temp2

	# change path
	cube_bo_c['path'].append('Bo\'')
	cube_heu = []
	cube_heu = cube_bo_c['left'] + cube_bo_c['top'] + cube_bo_c['right'] + cube_bo_c['front'] + cube_bo_c['bottom'] + cube_bo_c['back']
	diff = heuristic(cube_heu) + len(cube_bo_c['path'])
	queue.put((diff, cube_bo_c))
	# print(cube_bo_c['path'])

def rotate_back_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_ba = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_ba['back'][0]
	cube_ba['back'][0] = cube_ba['back'][1]
	cube_ba['back'][1] = cube_ba['back'][3]
	cube_ba['back'][3] = cube_ba['back'][2]
	cube_ba['back'][2] = temp
	
	# change side
	temp1 = cube_ba['bottom'][2]
	temp2 = cube_ba['bottom'][3]
	cube_ba['bottom'][2] = cube_ba['left'][1]
	cube_ba['bottom'][3] = cube_ba['left'][0]
	cube_ba['left'][0] = cube_ba['top'][0]
	cube_ba['left'][1] = cube_ba['top'][1]
	cube_ba['top'][0] = cube_ba['right'][0]
	cube_ba['top'][1] = cube_ba['right'][1]
	cube_ba['right'][0] = temp2
	cube_ba['right'][1] = temp1

	# change path
	cube_ba['path'].append('Ba')
	cube_heu = []
	cube_heu = cube_ba['left'] + cube_ba['top'] + cube_ba['right'] + cube_ba['front'] + cube_ba['bottom'] + cube_ba['back']
	diff = heuristic(cube_heu) + len(cube_ba['path'])
	queue.put((diff, cube_ba))
	# print(cube_ba['path'])

def rotate_back_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_ba_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_ba_c['back'][0]
	cube_ba_c['back'][0] = cube_ba_c['back'][2]
	cube_ba_c['back'][2] = cube_ba_c['back'][3]
	cube_ba_c['back'][3] = cube_ba_c['back'][1]
	cube_ba_c['back'][1] = temp
	
	# change side
	temp1 = cube_ba_c['bottom'][2]
	temp2 = cube_ba_c['bottom'][3]
	cube_ba_c['bottom'][2] = cube_ba_c['right'][1]
	cube_ba_c['bottom'][3] = cube_ba_c['right'][0]
	cube_ba_c['right'][0] = cube_ba_c['top'][0]
	cube_ba_c['right'][1] = cube_ba_c['top'][1]
	cube_ba_c['top'][0] = cube_ba_c['left'][0]
	cube_ba_c['top'][1] = cube_ba_c['left'][1]
	cube_ba_c['left'][0] = temp2
	cube_ba_c['left'][1] = temp1

	# change path
	cube_ba_c['path'].append('Ba\'')
	cube_heu = []
	cube_heu = cube_ba_c['left'] + cube_ba_c['top'] + cube_ba_c['right'] + cube_ba_c['front'] + cube_ba_c['bottom'] + cube_ba_c['back']
	diff = heuristic(cube_heu) + len(cube_ba_c['path'])
	queue.put((diff, cube_ba_c))
	# print(cube_ba_c['path'])

def rotate_left_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_l = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_l['left'][0]
	cube_l['left'][0] = cube_l['left'][2]
	cube_l['left'][2] = cube_l['left'][3]
	cube_l['left'][3] = cube_l['left'][1]
	cube_l['left'][1] = temp
	
	# change side
	temp1 = cube_l['bottom'][0]
	temp2 = cube_l['bottom'][2]
	cube_l['bottom'][0] = cube_l['front'][0]
	cube_l['bottom'][2] = cube_l['front'][2]
	cube_l['front'][0] = cube_l['top'][0]
	cube_l['front'][2] = cube_l['top'][2]
	cube_l['top'][0] = cube_l['back'][0]
	cube_l['top'][2] = cube_l['back'][2]
	cube_l['back'][0] = temp1
	cube_l['back'][2] = temp2

	# change path
	cube_l['path'].append('L')
	cube_heu = []
	cube_heu = cube_l['left'] + cube_l['top'] + cube_l['right'] + cube_l['front'] + cube_l['bottom'] + cube_l['back']
	diff = heuristic(cube_heu) + len(cube_l['path'])
	queue.put((diff, cube_l))
	# print(cube_l['path'])

def rotate_left_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_l_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_l_c['left'][0]
	cube_l_c['left'][0] = cube_l_c['left'][1]
	cube_l_c['left'][1] = cube_l_c['left'][3]
	cube_l_c['left'][3] = cube_l_c['left'][2]
	cube_l_c['left'][2] = temp
	
	# change side
	temp1 = cube_l_c['bottom'][0]
	temp2 = cube_l_c['bottom'][2]
	cube_l_c['bottom'][0] = cube_l_c['back'][0]
	cube_l_c['bottom'][2] = cube_l_c['back'][2]
	cube_l_c['back'][0] = cube_l_c['top'][0]
	cube_l_c['back'][2] = cube_l_c['top'][2]
	cube_l_c['top'][0] = cube_l_c['front'][0]
	cube_l_c['top'][2] = cube_l_c['front'][2]
	cube_l_c['front'][0] = temp1
	cube_l_c['front'][2] = temp2

	# change path
	cube_l_c['path'].append('L\'')
	cube_heu = []
	cube_heu = cube_l_c['left'] + cube_l_c['top'] + cube_l_c['right'] + cube_l_c['front'] + cube_l_c['bottom'] + cube_l_c['back']
	diff = heuristic(cube_heu) + len(cube_l_c['path'])
	queue.put((diff, cube_l_c))
	# print(cube_l_c['path'])

def rotate_right_cw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_r = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_r['right'][0]
	cube_r['right'][0] = cube_r['right'][2]
	cube_r['right'][2] = cube_r['right'][3]
	cube_r['right'][3] = cube_r['right'][1]
	cube_r['right'][1] = temp
	
	# change side
	temp1 = cube_r['bottom'][1]
	temp2 = cube_r['bottom'][3]
	cube_r['bottom'][1] = cube_r['back'][1]
	cube_r['bottom'][3] = cube_r['back'][3]
	cube_r['back'][1] = cube_r['top'][1]
	cube_r['back'][3] = cube_r['top'][3]
	cube_r['top'][1] = cube_r['front'][1]
	cube_r['top'][3] = cube_r['front'][3]
	cube_r['front'][1] = temp1
	cube_r['front'][3] = temp2

	# change path
	cube_r['path'].append('R')
	cube_heu = []
	cube_heu = cube_r['left'] + cube_r['top'] + cube_r['right'] + cube_r['front'] + cube_r['bottom'] + cube_r['back']
	diff = heuristic(cube_heu) + len(cube_r['path'])
	queue.put((diff, cube_r))
	# print(cube_r['path'])

def rotate_right_ccw(cube):
	# parse the input cube
	top = deepcopy(cube['top'])
	bottom = deepcopy(cube['bottom'])
	left = deepcopy(cube['left'])
	right = deepcopy(cube['right'])
	front = deepcopy(cube['front'])
	back = deepcopy(cube['back'])
	path = deepcopy(cube['path'])
	cube_r_c = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
	
	# change face
	temp = cube_r_c['right'][0]
	cube_r_c['right'][0] = cube_r_c['right'][1]
	cube_r_c['right'][1] = cube_r_c['right'][3]
	cube_r_c['right'][3] = cube_r_c['right'][2]
	cube_r_c['right'][2] = temp
	
	# change side
	temp1 = cube_r_c['bottom'][1]
	temp2 = cube_r_c['bottom'][3]
	cube_r_c['bottom'][1] = cube_r_c['front'][1]
	cube_r_c['bottom'][3] = cube_r_c['front'][3]
	cube_r_c['front'][1] = cube_r_c['top'][1]
	cube_r_c['front'][3] = cube_r_c['top'][3]
	cube_r_c['top'][1] = cube_r_c['back'][1]
	cube_r_c['top'][3] = cube_r_c['back'][3]
	cube_r_c['back'][1] = temp1
	cube_r_c['back'][3] = temp2

	# change path
	cube_r_c['path'].append('R\'')
	cube_heu = []
	cube_heu = cube_r_c['left'] + cube_r_c['top'] + cube_r_c['right'] + cube_r_c['front'] + cube_r_c['bottom'] + cube_r_c['back']
	diff = heuristic(cube_heu) + len(cube_r_c['path'])
	queue.put((diff, cube_r_c))
	# print(cube_r_c['path'])


def solveCube(name):
	start = time()
	with open(name) as file:
		rubik = [[str(char) for char in line.strip()] for line in file]
		left = [rubik[0][0],rubik[0][2],rubik[1][0],rubik[1][2]]
		top = [rubik[0][4],rubik[0][6],rubik[1][4],rubik[1][6]]
		right = [rubik[0][8],rubik[0][10],rubik[1][8],rubik[1][10]]
		front = [rubik[2][0],rubik[2][2],rubik[3][0],rubik[3][2]]
		bottom = [rubik[4][0],rubik[4][2],rubik[5][0],rubik[5][2]]
		back = [rubik[6][0],rubik[6][2],rubik[7][0],rubik[7][2]]
		path = []
		cube_list = left + top + right + front + bottom + back
		diff = heuristic(cube_list)
		cube_input = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
		queue.put((diff, cube_input))
		cost = 0

		# for i in range(5):
		# if queue:
		while queue:
			cube_cur = queue.get()[1]
			cost += 1
			if cube_cur['top'].count(cube_cur['top'][0]) == len(cube_cur['top']) and cube_cur['top'][0] is 'b':
				if cube_cur['bottom'].count(cube_cur['bottom'][0]) == len(cube_cur['bottom']) and cube_cur['bottom'][0] is 'y':
					if cube_cur['left'].count(cube_cur['left'][0]) == len(cube_cur['left']) and cube_cur['left'][0] is 'r':
						if cube_cur['right'].count(cube_cur['right'][0]) == len(cube_cur['right']) and cube_cur['right'][0] is 'g':
							if cube_cur['front'].count(cube_cur['front'][0]) == len(cube_cur['front']) and cube_cur['front'][0] is 'o':
								if cube_cur['back'].count(cube_cur['back'][0]) == len(cube_cur['back']) and cube_cur['back'][0] is 'p':
									print name
									print cube_cur['path']
									print cost
									print time()-start
									print("Done")
									break

			rotate_top_cw(cube_cur)
			rotate_top_ccw(cube_cur)
			rotate_bottom_cw(cube_cur)
			rotate_bottom_ccw(cube_cur)
			rotate_left_cw(cube_cur)
			rotate_left_ccw(cube_cur)
			rotate_right_cw(cube_cur)
			rotate_right_ccw(cube_cur)
			rotate_front_cw(cube_cur)
			rotate_front_ccw(cube_cur)
			rotate_back_cw(cube_cur)
			rotate_back_ccw(cube_cur)

# solveCube('goal.txt')
# solveCube('cube.txt')
solveCube('cube1_1.txt')
# solveCube('cube1_2.txt')
# solveCube('cube1_3.txt')