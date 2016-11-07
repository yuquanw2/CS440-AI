import Queue as Q
from copy import deepcopy
from time import time


queue = Q.PriorityQueue()
state = set()
def heuristic(cube_h):
	diff = [0] * 24
	goal = [None] * 24
	goal[0]= ['r','r','r','r','b','b','b','b','g','g','g','g','o','o','o','o','y','y','y','y','p','p','p','p']
	goal[1]= ['y','y','y','y','r','r','r','r','b','b','b','b','o','o','o','o','g','g','g','g','p','p','p','p']
	goal[2]= ['g','g','g','g','y','y','y','y','r','r','r','r','o','o','o','o','b','b','b','b','p','p','p','p']
	goal[3]= ['b','b','b','b','g','g','g','g','y','y','y','y','o','o','o','o','r','r','r','r','p','p','p','p']

	goal[4]= ['r','r','r','r','o','o','o','o','g','g','g','g','y','y','y','y','p','p','p','p','b','b','b','b']
	goal[5]= ['g','g','g','g','o','o','o','o','r','r','r','r','b','b','b','b','p','p','p','p','y','y','y','y']
	goal[6]= ['b','b','b','b','o','o','o','o','y','y','y','y','r','r','r','r','p','p','p','p','g','g','g','g']
	goal[7]= ['y','y','y','y','o','o','o','o','b','b','b','b','g','g','g','g','p','p','p','p','r','r','r','r']
	
	goal[8]= ['r','r','r','r','y','y','y','y','g','g','g','g','p','p','p','p','b','b','b','b','o','o','o','o']
	goal[9]= ['b','b','b','b','r','r','r','r','y','y','y','y','p','p','p','p','g','g','g','g','o','o','o','o']
	goal[10] = ['g','g','g','g','b','b','b','b','r','r','r','r','p','p','p','p','y','y','y','y','o','o','o','o']
	goal[11] = ['y','y','y','y','g','g','g','g','b','b','b','b','p','p','p','p','r','r','r','r','o','o','o','o']
	
	goal[12] = ['r','r','r','r','p','p','p','p','g','g','g','g','b','b','b','b','o','o','o','o','y','y','y','y']
	goal[13] = ['g','g','g','g','p','p','p','p','r','r','r','r','y','y','y','y','o','o','o','o','b','b','b','b']
	goal[14] = ['y','y','y','y','p','p','p','p','b','b','b','b','r','r','r','r','o','o','o','o','g','g','g','g']
	goal[15] = ['b','b','b','b','p','p','p','p','y','y','y','y','g','g','g','g','o','o','o','o','r','r','r','r']

	goal[16] = ['o','o','o','o','r','r','r','r','p','p','p','p','b','b','b','b','g','g','g','g','y','y','y','y']
	goal[17] = ['o','o','o','o','y','y','y','y','p','p','p','p','r','r','r','r','b','b','b','b','g','g','g','g']
	goal[18] = ['o','o','o','o','g','g','g','g','p','p','p','p','y','y','y','y','r','r','r','r','b','b','b','b']
	goal[19] = ['o','o','o','o','b','b','b','b','p','p','p','p','g','g','g','g','y','y','y','y','r','r','r','r']	
	
	goal[20] = ['p','p','p','p','r','r','r','r','o','o','o','o','y','y','y','y','g','g','g','g','b','b','b','b']
	goal[21] = ['p','p','p','p','b','b','b','b','o','o','o','o','r','r','r','r','y','y','y','y','g','g','g','g']
	goal[22] = ['p','p','p','p','g','g','g','g','o','o','o','o','b','b','b','b','r','r','r','r','y','y','y','y']
	goal[23] = ['p','p','p','p','y','y','y','y','o','o','o','o','g','g','g','g','b','b','b','b','r','r','r','r']

	for i in range(24):
		for j in range(24):
			if cube_h[j] is not goal[i][j]:
				diff[i] += 1
	# print diff
	return min(diff)/20

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
	
	# check repeated states
	cube_state_t = [None] * 24
	cube_state_t[0] = cube_t['left'] + cube_t['top'] + cube_t['right'] + cube_t['front'] + cube_t['bottom'] + cube_t['back']
	cube_state_t[1] = cube_t['bottom'] + cube_t['left'] + cube_t['top'] + cube_t['front'] + cube_t['right'] + cube_t['back']
	cube_state_t[2] = cube_t['right'] + cube_t['bottom'] + cube_t['left'] + cube_t['front'] + cube_t['top'] + cube_t['back']
	cube_state_t[3] = cube_t['top'] + cube_t['right'] + cube_t['bottom'] + cube_t['front'] + cube_t['left'] + cube_t['back']

	cube_state_t[4] = cube_t['left'] + cube_t['front'] + cube_t['right'] + cube_t['bottom'] + cube_t['back'] + cube_t['top']
	cube_state_t[5] = cube_t['bottom'] + cube_t['front'] + cube_t['top'] + cube_t['right'] + cube_t['back'] + cube_t['left']
	cube_state_t[6] = cube_t['right'] + cube_t['front'] + cube_t['left'] + cube_t['top'] + cube_t['back'] + cube_t['bottom']
	cube_state_t[7] = cube_t['top'] + cube_t['front'] + cube_t['bottom'] + cube_t['left'] + cube_t['back'] + cube_t['right']
	
	cube_state_t[8] = cube_t['left'] + cube_t['bottom'] + cube_t['right'] + cube_t['back'] + cube_t['top'] + cube_t['front']
	cube_state_t[9] = cube_t['top'] + cube_t['left'] + cube_t['bottom'] + cube_t['back'] + cube_t['right'] + cube_t['front']
	cube_state_t[10] = cube_t['right'] + cube_t['top'] + cube_t['left'] + cube_t['back'] + cube_t['bottom'] + cube_t['front']
	cube_state_t[11] = cube_t['bottom'] + cube_t['right'] + cube_t['top'] + cube_t['back'] + cube_t['left'] + cube_t['front']
	
	cube_state_t[12] = cube_t['left'] + cube_t['back'] + cube_t['right'] + cube_t['top'] + cube_t['front'] + cube_t['bottom']
	cube_state_t[13] = cube_t['top'] + cube_t['back'] + cube_t['bottom'] + cube_t['right'] + cube_t['front'] + cube_t['left']
	cube_state_t[14] = cube_t['right'] + cube_t['back'] + cube_t['left'] + cube_t['bottom'] + cube_t['front'] + cube_t['top']
	cube_state_t[15] = cube_t['bottom'] + cube_t['back'] + cube_t['top'] + cube_t['left'] + cube_t['front'] + cube_t['right']
	
	cube_state_t[16] = cube_t['front'] + cube_t['top'] + cube_t['back'] + cube_t['right'] + cube_t['bottom'] + cube_t['left']
	cube_state_t[17] = cube_t['front'] + cube_t['left'] + cube_t['back'] + cube_t['top'] + cube_t['right'] + cube_t['bottom']
	cube_state_t[18] = cube_t['front'] + cube_t['bottom'] + cube_t['back'] + cube_t['left'] + cube_t['top'] + cube_t['right']
	cube_state_t[19] = cube_t['front'] + cube_t['right'] + cube_t['back'] + cube_t['bottom'] + cube_t['left'] + cube_t['top']
	
	cube_state_t[20] = cube_t['back'] + cube_t['top'] + cube_t['front'] + cube_t['left'] + cube_t['bottom'] + cube_t['right']
	cube_state_t[21] = cube_t['back'] + cube_t['left'] + cube_t['front'] + cube_t['bottom'] + cube_t['right'] + cube_t['top']
	cube_state_t[22] = cube_t['back'] + cube_t['bottom'] + cube_t['front'] + cube_t['right'] + cube_t['top'] + cube_t['left']
	cube_state_t[23] = cube_t['back'] + cube_t['right'] + cube_t['front'] + cube_t['top'] + cube_t['left'] + cube_t['bottom']
	
	cube_state_str_t = [None] * 24
	for i in range(24):
		cube_state_str_t[i] = ''.join(cube_state_t[i])
		if cube_state_str_t[i] in state:
			return

	queue.put((diff, cube_t))
	state.add(cube_state_str_t[0])
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
	
	# check repeated states
	cube_state_t_c = [None] * 24
	cube_state_t_c[0] = cube_t_c['left'] + cube_t_c['top'] + cube_t_c['right'] + cube_t_c['front'] + cube_t_c['bottom'] + cube_t_c['back']
	cube_state_t_c[1] = cube_t_c['bottom'] + cube_t_c['left'] + cube_t_c['top'] + cube_t_c['front'] + cube_t_c['right'] + cube_t_c['back']
	cube_state_t_c[2] = cube_t_c['right'] + cube_t_c['bottom'] + cube_t_c['left'] + cube_t_c['front'] + cube_t_c['top'] + cube_t_c['back']
	cube_state_t_c[3] = cube_t_c['top'] + cube_t_c['right'] + cube_t_c['bottom'] + cube_t_c['front'] + cube_t_c['left'] + cube_t_c['back']

	cube_state_t_c[4] = cube_t_c['left'] + cube_t_c['front'] + cube_t_c['right'] + cube_t_c['bottom'] + cube_t_c['back'] + cube_t_c['top']
	cube_state_t_c[5] = cube_t_c['bottom'] + cube_t_c['front'] + cube_t_c['top'] + cube_t_c['right'] + cube_t_c['back'] + cube_t_c['left']
	cube_state_t_c[6] = cube_t_c['right'] + cube_t_c['front'] + cube_t_c['left'] + cube_t_c['top'] + cube_t_c['back'] + cube_t_c['bottom']
	cube_state_t_c[7] = cube_t_c['top'] + cube_t_c['front'] + cube_t_c['bottom'] + cube_t_c['left'] + cube_t_c['back'] + cube_t_c['right']
	
	cube_state_t_c[8] = cube_t_c['left'] + cube_t_c['bottom'] + cube_t_c['right'] + cube_t_c['back'] + cube_t_c['top'] + cube_t_c['front']
	cube_state_t_c[9] = cube_t_c['top'] + cube_t_c['left'] + cube_t_c['bottom'] + cube_t_c['back'] + cube_t_c['right'] + cube_t_c['front']
	cube_state_t_c[10] = cube_t_c['right'] + cube_t_c['top'] + cube_t_c['left'] + cube_t_c['back'] + cube_t_c['bottom'] + cube_t_c['front']
	cube_state_t_c[11] = cube_t_c['bottom'] + cube_t_c['right'] + cube_t_c['top'] + cube_t_c['back'] + cube_t_c['left'] + cube_t_c['front']
	
	cube_state_t_c[12] = cube_t_c['left'] + cube_t_c['back'] + cube_t_c['right'] + cube_t_c['top'] + cube_t_c['front'] + cube_t_c['bottom']
	cube_state_t_c[13] = cube_t_c['top'] + cube_t_c['back'] + cube_t_c['bottom'] + cube_t_c['right'] + cube_t_c['front'] + cube_t_c['left']
	cube_state_t_c[14] = cube_t_c['right'] + cube_t_c['back'] + cube_t_c['left'] + cube_t_c['bottom'] + cube_t_c['front'] + cube_t_c['top']
	cube_state_t_c[15] = cube_t_c['bottom'] + cube_t_c['back'] + cube_t_c['top'] + cube_t_c['left'] + cube_t_c['front'] + cube_t_c['right']
	
	cube_state_t_c[16] = cube_t_c['front'] + cube_t_c['top'] + cube_t_c['back'] + cube_t_c['right'] + cube_t_c['bottom'] + cube_t_c['left']
	cube_state_t_c[17] = cube_t_c['front'] + cube_t_c['left'] + cube_t_c['back'] + cube_t_c['top'] + cube_t_c['right'] + cube_t_c['bottom']
	cube_state_t_c[18] = cube_t_c['front'] + cube_t_c['bottom'] + cube_t_c['back'] + cube_t_c['left'] + cube_t_c['top'] + cube_t_c['right']
	cube_state_t_c[19] = cube_t_c['front'] + cube_t_c['right'] + cube_t_c['back'] + cube_t_c['bottom'] + cube_t_c['left'] + cube_t_c['top']
	
	cube_state_t_c[20] = cube_t_c['back'] + cube_t_c['top'] + cube_t_c['front'] + cube_t_c['left'] + cube_t_c['bottom'] + cube_t_c['right']
	cube_state_t_c[21] = cube_t_c['back'] + cube_t_c['left'] + cube_t_c['front'] + cube_t_c['bottom'] + cube_t_c['right'] + cube_t_c['top']
	cube_state_t_c[22] = cube_t_c['back'] + cube_t_c['bottom'] + cube_t_c['front'] + cube_t_c['right'] + cube_t_c['top'] + cube_t_c['left']
	cube_state_t_c[23] = cube_t_c['back'] + cube_t_c['right'] + cube_t_c['front'] + cube_t_c['top'] + cube_t_c['left'] + cube_t_c['bottom']
	
	cube_state_str_t_c = [None] * 24
	for i in range(24):
		cube_state_str_t_c[i] = ''.join(cube_state_t_c[i])
		if cube_state_str_t_c[i] in state:
			return

	queue.put((diff, cube_t_c))
	state.add(cube_state_str_t_c[0])
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
	
	# check repeated states
	cube_state_f = [None] * 24
	cube_state_f[0] = cube_f['left'] + cube_f['top'] + cube_f['right'] + cube_f['front'] + cube_f['bottom'] + cube_f['back']
	cube_state_f[1] = cube_f['bottom'] + cube_f['left'] + cube_f['top'] + cube_f['front'] + cube_f['right'] + cube_f['back']
	cube_state_f[2] = cube_f['right'] + cube_f['bottom'] + cube_f['left'] + cube_f['front'] + cube_f['top'] + cube_f['back']
	cube_state_f[3] = cube_f['top'] + cube_f['right'] + cube_f['bottom'] + cube_f['front'] + cube_f['left'] + cube_f['back']

	cube_state_f[4] = cube_f['left'] + cube_f['front'] + cube_f['right'] + cube_f['bottom'] + cube_f['back'] + cube_f['top']
	cube_state_f[5] = cube_f['bottom'] + cube_f['front'] + cube_f['top'] + cube_f['right'] + cube_f['back'] + cube_f['left']
	cube_state_f[6] = cube_f['right'] + cube_f['front'] + cube_f['left'] + cube_f['top'] + cube_f['back'] + cube_f['bottom']
	cube_state_f[7] = cube_f['top'] + cube_f['front'] + cube_f['bottom'] + cube_f['left'] + cube_f['back'] + cube_f['right']
	
	cube_state_f[8] = cube_f['left'] + cube_f['bottom'] + cube_f['right'] + cube_f['back'] + cube_f['top'] + cube_f['front']
	cube_state_f[9] = cube_f['top'] + cube_f['left'] + cube_f['bottom'] + cube_f['back'] + cube_f['right'] + cube_f['front']
	cube_state_f[10] = cube_f['right'] + cube_f['top'] + cube_f['left'] + cube_f['back'] + cube_f['bottom'] + cube_f['front']
	cube_state_f[11] = cube_f['bottom'] + cube_f['right'] + cube_f['top'] + cube_f['back'] + cube_f['left'] + cube_f['front']
	
	cube_state_f[12] = cube_f['left'] + cube_f['back'] + cube_f['right'] + cube_f['top'] + cube_f['front'] + cube_f['bottom']
	cube_state_f[13] = cube_f['top'] + cube_f['back'] + cube_f['bottom'] + cube_f['right'] + cube_f['front'] + cube_f['left']
	cube_state_f[14] = cube_f['right'] + cube_f['back'] + cube_f['left'] + cube_f['bottom'] + cube_f['front'] + cube_f['top']
	cube_state_f[15] = cube_f['bottom'] + cube_f['back'] + cube_f['top'] + cube_f['left'] + cube_f['front'] + cube_f['right']
	
	cube_state_f[16] = cube_f['front'] + cube_f['top'] + cube_f['back'] + cube_f['right'] + cube_f['bottom'] + cube_f['left']
	cube_state_f[17] = cube_f['front'] + cube_f['left'] + cube_f['back'] + cube_f['top'] + cube_f['right'] + cube_f['bottom']
	cube_state_f[18] = cube_f['front'] + cube_f['bottom'] + cube_f['back'] + cube_f['left'] + cube_f['top'] + cube_f['right']
	cube_state_f[19] = cube_f['front'] + cube_f['right'] + cube_f['back'] + cube_f['bottom'] + cube_f['left'] + cube_f['top']
	
	cube_state_f[20] = cube_f['back'] + cube_f['top'] + cube_f['front'] + cube_f['left'] + cube_f['bottom'] + cube_f['right']
	cube_state_f[21] = cube_f['back'] + cube_f['left'] + cube_f['front'] + cube_f['bottom'] + cube_f['right'] + cube_f['top']
	cube_state_f[22] = cube_f['back'] + cube_f['bottom'] + cube_f['front'] + cube_f['right'] + cube_f['top'] + cube_f['left']
	cube_state_f[23] = cube_f['back'] + cube_f['right'] + cube_f['front'] + cube_f['top'] + cube_f['left'] + cube_f['bottom']
	
	cube_state_str_f = [None] * 24
	for i in range(24):
		cube_state_str_f[i] = ''.join(cube_state_f[i])
		if cube_state_str_f[i] in state:
			return

	queue.put((diff, cube_f))
	state.add(cube_state_str_f[0])
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

	# check repeated states
	cube_state_f_c = [None] * 24
	cube_state_f_c[0] = cube_f_c['left'] + cube_f_c['top'] + cube_f_c['right'] + cube_f_c['front'] + cube_f_c['bottom'] + cube_f_c['back']
	cube_state_f_c[1] = cube_f_c['bottom'] + cube_f_c['left'] + cube_f_c['top'] + cube_f_c['front'] + cube_f_c['right'] + cube_f_c['back']
	cube_state_f_c[2] = cube_f_c['right'] + cube_f_c['bottom'] + cube_f_c['left'] + cube_f_c['front'] + cube_f_c['top'] + cube_f_c['back']
	cube_state_f_c[3] = cube_f_c['top'] + cube_f_c['right'] + cube_f_c['bottom'] + cube_f_c['front'] + cube_f_c['left'] + cube_f_c['back']

	cube_state_f_c[4] = cube_f_c['left'] + cube_f_c['front'] + cube_f_c['right'] + cube_f_c['bottom'] + cube_f_c['back'] + cube_f_c['top']
	cube_state_f_c[5] = cube_f_c['bottom'] + cube_f_c['front'] + cube_f_c['top'] + cube_f_c['right'] + cube_f_c['back'] + cube_f_c['left']
	cube_state_f_c[6] = cube_f_c['right'] + cube_f_c['front'] + cube_f_c['left'] + cube_f_c['top'] + cube_f_c['back'] + cube_f_c['bottom']
	cube_state_f_c[7] = cube_f_c['top'] + cube_f_c['front'] + cube_f_c['bottom'] + cube_f_c['left'] + cube_f_c['back'] + cube_f_c['right']
	
	cube_state_f_c[8] = cube_f_c['left'] + cube_f_c['bottom'] + cube_f_c['right'] + cube_f_c['back'] + cube_f_c['top'] + cube_f_c['front']
	cube_state_f_c[9] = cube_f_c['top'] + cube_f_c['left'] + cube_f_c['bottom'] + cube_f_c['back'] + cube_f_c['right'] + cube_f_c['front']
	cube_state_f_c[10] = cube_f_c['right'] + cube_f_c['top'] + cube_f_c['left'] + cube_f_c['back'] + cube_f_c['bottom'] + cube_f_c['front']
	cube_state_f_c[11] = cube_f_c['bottom'] + cube_f_c['right'] + cube_f_c['top'] + cube_f_c['back'] + cube_f_c['left'] + cube_f_c['front']
	
	cube_state_f_c[12] = cube_f_c['left'] + cube_f_c['back'] + cube_f_c['right'] + cube_f_c['top'] + cube_f_c['front'] + cube_f_c['bottom']
	cube_state_f_c[13] = cube_f_c['top'] + cube_f_c['back'] + cube_f_c['bottom'] + cube_f_c['right'] + cube_f_c['front'] + cube_f_c['left']
	cube_state_f_c[14] = cube_f_c['right'] + cube_f_c['back'] + cube_f_c['left'] + cube_f_c['bottom'] + cube_f_c['front'] + cube_f_c['top']
	cube_state_f_c[15] = cube_f_c['bottom'] + cube_f_c['back'] + cube_f_c['top'] + cube_f_c['left'] + cube_f_c['front'] + cube_f_c['right']
	
	cube_state_f_c[16] = cube_f_c['front'] + cube_f_c['top'] + cube_f_c['back'] + cube_f_c['right'] + cube_f_c['bottom'] + cube_f_c['left']
	cube_state_f_c[17] = cube_f_c['front'] + cube_f_c['left'] + cube_f_c['back'] + cube_f_c['top'] + cube_f_c['right'] + cube_f_c['bottom']
	cube_state_f_c[18] = cube_f_c['front'] + cube_f_c['bottom'] + cube_f_c['back'] + cube_f_c['left'] + cube_f_c['top'] + cube_f_c['right']
	cube_state_f_c[19] = cube_f_c['front'] + cube_f_c['right'] + cube_f_c['back'] + cube_f_c['bottom'] + cube_f_c['left'] + cube_f_c['top']
	
	cube_state_f_c[20] = cube_f_c['back'] + cube_f_c['top'] + cube_f_c['front'] + cube_f_c['left'] + cube_f_c['bottom'] + cube_f_c['right']
	cube_state_f_c[21] = cube_f_c['back'] + cube_f_c['left'] + cube_f_c['front'] + cube_f_c['bottom'] + cube_f_c['right'] + cube_f_c['top']
	cube_state_f_c[22] = cube_f_c['back'] + cube_f_c['bottom'] + cube_f_c['front'] + cube_f_c['right'] + cube_f_c['top'] + cube_f_c['left']
	cube_state_f_c[23] = cube_f_c['back'] + cube_f_c['right'] + cube_f_c['front'] + cube_f_c['top'] + cube_f_c['left'] + cube_f_c['bottom']
	
	cube_state_str_f_c = [None] * 24
	for i in range(24):
		cube_state_str_f_c[i] = ''.join(cube_state_f_c[i])
		if cube_state_str_f_c[i] in state:
			return

	queue.put((diff, cube_f_c))
	state.add(cube_state_str_f_c[0])
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
	
	# check repeated states
	cube_state_bo = [None] * 24
	cube_state_bo[0] = cube_bo['left'] + cube_bo['top'] + cube_bo['right'] + cube_bo['front'] + cube_bo['bottom'] + cube_bo['back']
	cube_state_bo[1] = cube_bo['bottom'] + cube_bo['left'] + cube_bo['top'] + cube_bo['front'] + cube_bo['right'] + cube_bo['back']
	cube_state_bo[2] = cube_bo['right'] + cube_bo['bottom'] + cube_bo['left'] + cube_bo['front'] + cube_bo['top'] + cube_bo['back']
	cube_state_bo[3] = cube_bo['top'] + cube_bo['right'] + cube_bo['bottom'] + cube_bo['front'] + cube_bo['left'] + cube_bo['back']

	cube_state_bo[4] = cube_bo['left'] + cube_bo['front'] + cube_bo['right'] + cube_bo['bottom'] + cube_bo['back'] + cube_bo['top']
	cube_state_bo[5] = cube_bo['bottom'] + cube_bo['front'] + cube_bo['top'] + cube_bo['right'] + cube_bo['back'] + cube_bo['left']
	cube_state_bo[6] = cube_bo['right'] + cube_bo['front'] + cube_bo['left'] + cube_bo['top'] + cube_bo['back'] + cube_bo['bottom']
	cube_state_bo[7] = cube_bo['top'] + cube_bo['front'] + cube_bo['bottom'] + cube_bo['left'] + cube_bo['back'] + cube_bo['right']
	
	cube_state_bo[8] = cube_bo['left'] + cube_bo['bottom'] + cube_bo['right'] + cube_bo['back'] + cube_bo['top'] + cube_bo['front']
	cube_state_bo[9] = cube_bo['top'] + cube_bo['left'] + cube_bo['bottom'] + cube_bo['back'] + cube_bo['right'] + cube_bo['front']
	cube_state_bo[10] = cube_bo['right'] + cube_bo['top'] + cube_bo['left'] + cube_bo['back'] + cube_bo['bottom'] + cube_bo['front']
	cube_state_bo[11] = cube_bo['bottom'] + cube_bo['right'] + cube_bo['top'] + cube_bo['back'] + cube_bo['left'] + cube_bo['front']
	
	cube_state_bo[12] = cube_bo['left'] + cube_bo['back'] + cube_bo['right'] + cube_bo['top'] + cube_bo['front'] + cube_bo['bottom']
	cube_state_bo[13] = cube_bo['top'] + cube_bo['back'] + cube_bo['bottom'] + cube_bo['right'] + cube_bo['front'] + cube_bo['left']
	cube_state_bo[14] = cube_bo['right'] + cube_bo['back'] + cube_bo['left'] + cube_bo['bottom'] + cube_bo['front'] + cube_bo['top']
	cube_state_bo[15] = cube_bo['bottom'] + cube_bo['back'] + cube_bo['top'] + cube_bo['left'] + cube_bo['front'] + cube_bo['right']
	
	cube_state_bo[16] = cube_bo['front'] + cube_bo['top'] + cube_bo['back'] + cube_bo['right'] + cube_bo['bottom'] + cube_bo['left']
	cube_state_bo[17] = cube_bo['front'] + cube_bo['left'] + cube_bo['back'] + cube_bo['top'] + cube_bo['right'] + cube_bo['bottom']
	cube_state_bo[18] = cube_bo['front'] + cube_bo['bottom'] + cube_bo['back'] + cube_bo['left'] + cube_bo['top'] + cube_bo['right']
	cube_state_bo[19] = cube_bo['front'] + cube_bo['right'] + cube_bo['back'] + cube_bo['bottom'] + cube_bo['left'] + cube_bo['top']
	
	cube_state_bo[20] = cube_bo['back'] + cube_bo['top'] + cube_bo['front'] + cube_bo['left'] + cube_bo['bottom'] + cube_bo['right']
	cube_state_bo[21] = cube_bo['back'] + cube_bo['left'] + cube_bo['front'] + cube_bo['bottom'] + cube_bo['right'] + cube_bo['top']
	cube_state_bo[22] = cube_bo['back'] + cube_bo['bottom'] + cube_bo['front'] + cube_bo['right'] + cube_bo['top'] + cube_bo['left']
	cube_state_bo[23] = cube_bo['back'] + cube_bo['right'] + cube_bo['front'] + cube_bo['top'] + cube_bo['left'] + cube_bo['bottom']
	
	cube_state_str_bo = [None] * 24
	for i in range(24):
		cube_state_str_bo[i] = ''.join(cube_state_bo[i])
		if cube_state_str_bo[i] in state:
			return

	queue.put((diff, cube_bo))
	state.add(cube_state_str_bo[0])
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
	
	# check repeated states
	cube_state_bo_c = [None] * 24
	cube_state_bo_c[0] = cube_bo_c['left'] + cube_bo_c['top'] + cube_bo_c['right'] + cube_bo_c['front'] + cube_bo_c['bottom'] + cube_bo_c['back']
	cube_state_bo_c[1] = cube_bo_c['bottom'] + cube_bo_c['left'] + cube_bo_c['top'] + cube_bo_c['front'] + cube_bo_c['right'] + cube_bo_c['back']
	cube_state_bo_c[2] = cube_bo_c['right'] + cube_bo_c['bottom'] + cube_bo_c['left'] + cube_bo_c['front'] + cube_bo_c['top'] + cube_bo_c['back']
	cube_state_bo_c[3] = cube_bo_c['top'] + cube_bo_c['right'] + cube_bo_c['bottom'] + cube_bo_c['front'] + cube_bo_c['left'] + cube_bo_c['back']

	cube_state_bo_c[4] = cube_bo_c['left'] + cube_bo_c['front'] + cube_bo_c['right'] + cube_bo_c['bottom'] + cube_bo_c['back'] + cube_bo_c['top']
	cube_state_bo_c[5] = cube_bo_c['bottom'] + cube_bo_c['front'] + cube_bo_c['top'] + cube_bo_c['right'] + cube_bo_c['back'] + cube_bo_c['left']
	cube_state_bo_c[6] = cube_bo_c['right'] + cube_bo_c['front'] + cube_bo_c['left'] + cube_bo_c['top'] + cube_bo_c['back'] + cube_bo_c['bottom']
	cube_state_bo_c[7] = cube_bo_c['top'] + cube_bo_c['front'] + cube_bo_c['bottom'] + cube_bo_c['left'] + cube_bo_c['back'] + cube_bo_c['right']
	
	cube_state_bo_c[8] = cube_bo_c['left'] + cube_bo_c['bottom'] + cube_bo_c['right'] + cube_bo_c['back'] + cube_bo_c['top'] + cube_bo_c['front']
	cube_state_bo_c[9] = cube_bo_c['top'] + cube_bo_c['left'] + cube_bo_c['bottom'] + cube_bo_c['back'] + cube_bo_c['right'] + cube_bo_c['front']
	cube_state_bo_c[10] = cube_bo_c['right'] + cube_bo_c['top'] + cube_bo_c['left'] + cube_bo_c['back'] + cube_bo_c['bottom'] + cube_bo_c['front']
	cube_state_bo_c[11] = cube_bo_c['bottom'] + cube_bo_c['right'] + cube_bo_c['top'] + cube_bo_c['back'] + cube_bo_c['left'] + cube_bo_c['front']
	
	cube_state_bo_c[12] = cube_bo_c['left'] + cube_bo_c['back'] + cube_bo_c['right'] + cube_bo_c['top'] + cube_bo_c['front'] + cube_bo_c['bottom']
	cube_state_bo_c[13] = cube_bo_c['top'] + cube_bo_c['back'] + cube_bo_c['bottom'] + cube_bo_c['right'] + cube_bo_c['front'] + cube_bo_c['left']
	cube_state_bo_c[14] = cube_bo_c['right'] + cube_bo_c['back'] + cube_bo_c['left'] + cube_bo_c['bottom'] + cube_bo_c['front'] + cube_bo_c['top']
	cube_state_bo_c[15] = cube_bo_c['bottom'] + cube_bo_c['back'] + cube_bo_c['top'] + cube_bo_c['left'] + cube_bo_c['front'] + cube_bo_c['right']
	
	cube_state_bo_c[16] = cube_bo_c['front'] + cube_bo_c['top'] + cube_bo_c['back'] + cube_bo_c['right'] + cube_bo_c['bottom'] + cube_bo_c['left']
	cube_state_bo_c[17] = cube_bo_c['front'] + cube_bo_c['left'] + cube_bo_c['back'] + cube_bo_c['top'] + cube_bo_c['right'] + cube_bo_c['bottom']
	cube_state_bo_c[18] = cube_bo_c['front'] + cube_bo_c['bottom'] + cube_bo_c['back'] + cube_bo_c['left'] + cube_bo_c['top'] + cube_bo_c['right']
	cube_state_bo_c[19] = cube_bo_c['front'] + cube_bo_c['right'] + cube_bo_c['back'] + cube_bo_c['bottom'] + cube_bo_c['left'] + cube_bo_c['top']
	
	cube_state_bo_c[20] = cube_bo_c['back'] + cube_bo_c['top'] + cube_bo_c['front'] + cube_bo_c['left'] + cube_bo_c['bottom'] + cube_bo_c['right']
	cube_state_bo_c[21] = cube_bo_c['back'] + cube_bo_c['left'] + cube_bo_c['front'] + cube_bo_c['bottom'] + cube_bo_c['right'] + cube_bo_c['top']
	cube_state_bo_c[22] = cube_bo_c['back'] + cube_bo_c['bottom'] + cube_bo_c['front'] + cube_bo_c['right'] + cube_bo_c['top'] + cube_bo_c['left']
	cube_state_bo_c[23] = cube_bo_c['back'] + cube_bo_c['right'] + cube_bo_c['front'] + cube_bo_c['top'] + cube_bo_c['left'] + cube_bo_c['bottom']
	
	cube_state_str_bo = [None] * 24
	for i in range(24):
		cube_state_str_bo[i] = ''.join(cube_state_bo_c[i])
		if cube_state_str_bo[i] in state:
			return

	queue.put((diff, cube_bo_c))
	state.add(cube_state_str_bo[0])
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
	
	# check repeated states
	cube_state_ba = [None] * 24
	cube_state_ba[0] = cube_ba['left'] + cube_ba['top'] + cube_ba['right'] + cube_ba['front'] + cube_ba['bottom'] + cube_ba['back']
	cube_state_ba[1] = cube_ba['bottom'] + cube_ba['left'] + cube_ba['top'] + cube_ba['front'] + cube_ba['right'] + cube_ba['back']
	cube_state_ba[2] = cube_ba['right'] + cube_ba['bottom'] + cube_ba['left'] + cube_ba['front'] + cube_ba['top'] + cube_ba['back']
	cube_state_ba[3] = cube_ba['top'] + cube_ba['right'] + cube_ba['bottom'] + cube_ba['front'] + cube_ba['left'] + cube_ba['back']

	cube_state_ba[4] = cube_ba['left'] + cube_ba['front'] + cube_ba['right'] + cube_ba['bottom'] + cube_ba['back'] + cube_ba['top']
	cube_state_ba[5] = cube_ba['bottom'] + cube_ba['front'] + cube_ba['top'] + cube_ba['right'] + cube_ba['back'] + cube_ba['left']
	cube_state_ba[6] = cube_ba['right'] + cube_ba['front'] + cube_ba['left'] + cube_ba['top'] + cube_ba['back'] + cube_ba['bottom']
	cube_state_ba[7] = cube_ba['top'] + cube_ba['front'] + cube_ba['bottom'] + cube_ba['left'] + cube_ba['back'] + cube_ba['right']
	
	cube_state_ba[8] = cube_ba['left'] + cube_ba['bottom'] + cube_ba['right'] + cube_ba['back'] + cube_ba['top'] + cube_ba['front']
	cube_state_ba[9] = cube_ba['top'] + cube_ba['left'] + cube_ba['bottom'] + cube_ba['back'] + cube_ba['right'] + cube_ba['front']
	cube_state_ba[10] = cube_ba['right'] + cube_ba['top'] + cube_ba['left'] + cube_ba['back'] + cube_ba['bottom'] + cube_ba['front']
	cube_state_ba[11] = cube_ba['bottom'] + cube_ba['right'] + cube_ba['top'] + cube_ba['back'] + cube_ba['left'] + cube_ba['front']
	
	cube_state_ba[12] = cube_ba['left'] + cube_ba['back'] + cube_ba['right'] + cube_ba['top'] + cube_ba['front'] + cube_ba['bottom']
	cube_state_ba[13] = cube_ba['top'] + cube_ba['back'] + cube_ba['bottom'] + cube_ba['right'] + cube_ba['front'] + cube_ba['left']
	cube_state_ba[14] = cube_ba['right'] + cube_ba['back'] + cube_ba['left'] + cube_ba['bottom'] + cube_ba['front'] + cube_ba['top']
	cube_state_ba[15] = cube_ba['bottom'] + cube_ba['back'] + cube_ba['top'] + cube_ba['left'] + cube_ba['front'] + cube_ba['right']
	
	cube_state_ba[16] = cube_ba['front'] + cube_ba['top'] + cube_ba['back'] + cube_ba['right'] + cube_ba['bottom'] + cube_ba['left']
	cube_state_ba[17] = cube_ba['front'] + cube_ba['left'] + cube_ba['back'] + cube_ba['top'] + cube_ba['right'] + cube_ba['bottom']
	cube_state_ba[18] = cube_ba['front'] + cube_ba['bottom'] + cube_ba['back'] + cube_ba['left'] + cube_ba['top'] + cube_ba['right']
	cube_state_ba[19] = cube_ba['front'] + cube_ba['right'] + cube_ba['back'] + cube_ba['bottom'] + cube_ba['left'] + cube_ba['top']
	
	cube_state_ba[20] = cube_ba['back'] + cube_ba['top'] + cube_ba['front'] + cube_ba['left'] + cube_ba['bottom'] + cube_ba['right']
	cube_state_ba[21] = cube_ba['back'] + cube_ba['left'] + cube_ba['front'] + cube_ba['bottom'] + cube_ba['right'] + cube_ba['top']
	cube_state_ba[22] = cube_ba['back'] + cube_ba['bottom'] + cube_ba['front'] + cube_ba['right'] + cube_ba['top'] + cube_ba['left']
	cube_state_ba[23] = cube_ba['back'] + cube_ba['right'] + cube_ba['front'] + cube_ba['top'] + cube_ba['left'] + cube_ba['bottom']
	
	cube_state_str_ba = [None] * 24
	for i in range(24):
		cube_state_str_ba[i] = ''.join(cube_state_ba[i])
		if cube_state_str_ba[i] in state:
			return

	queue.put((diff, cube_ba))
	state.add(cube_state_str_ba[0])
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
	
	# check repeated states
	cube_state_ba_c = [None] * 24
	cube_state_ba_c[0] = cube_ba_c['left'] + cube_ba_c['top'] + cube_ba_c['right'] + cube_ba_c['front'] + cube_ba_c['bottom'] + cube_ba_c['back']
	cube_state_ba_c[1] = cube_ba_c['bottom'] + cube_ba_c['left'] + cube_ba_c['top'] + cube_ba_c['front'] + cube_ba_c['right'] + cube_ba_c['back']
	cube_state_ba_c[2] = cube_ba_c['right'] + cube_ba_c['bottom'] + cube_ba_c['left'] + cube_ba_c['front'] + cube_ba_c['top'] + cube_ba_c['back']
	cube_state_ba_c[3] = cube_ba_c['top'] + cube_ba_c['right'] + cube_ba_c['bottom'] + cube_ba_c['front'] + cube_ba_c['left'] + cube_ba_c['back']

	cube_state_ba_c[4] = cube_ba_c['left'] + cube_ba_c['front'] + cube_ba_c['right'] + cube_ba_c['bottom'] + cube_ba_c['back'] + cube_ba_c['top']
	cube_state_ba_c[5] = cube_ba_c['bottom'] + cube_ba_c['front'] + cube_ba_c['top'] + cube_ba_c['right'] + cube_ba_c['back'] + cube_ba_c['left']
	cube_state_ba_c[6] = cube_ba_c['right'] + cube_ba_c['front'] + cube_ba_c['left'] + cube_ba_c['top'] + cube_ba_c['back'] + cube_ba_c['bottom']
	cube_state_ba_c[7] = cube_ba_c['top'] + cube_ba_c['front'] + cube_ba_c['bottom'] + cube_ba_c['left'] + cube_ba_c['back'] + cube_ba_c['right']
	
	cube_state_ba_c[8] = cube_ba_c['left'] + cube_ba_c['bottom'] + cube_ba_c['right'] + cube_ba_c['back'] + cube_ba_c['top'] + cube_ba_c['front']
	cube_state_ba_c[9] = cube_ba_c['top'] + cube_ba_c['left'] + cube_ba_c['bottom'] + cube_ba_c['back'] + cube_ba_c['right'] + cube_ba_c['front']
	cube_state_ba_c[10] = cube_ba_c['right'] + cube_ba_c['top'] + cube_ba_c['left'] + cube_ba_c['back'] + cube_ba_c['bottom'] + cube_ba_c['front']
	cube_state_ba_c[11] = cube_ba_c['bottom'] + cube_ba_c['right'] + cube_ba_c['top'] + cube_ba_c['back'] + cube_ba_c['left'] + cube_ba_c['front']
	
	cube_state_ba_c[12] = cube_ba_c['left'] + cube_ba_c['back'] + cube_ba_c['right'] + cube_ba_c['top'] + cube_ba_c['front'] + cube_ba_c['bottom']
	cube_state_ba_c[13] = cube_ba_c['top'] + cube_ba_c['back'] + cube_ba_c['bottom'] + cube_ba_c['right'] + cube_ba_c['front'] + cube_ba_c['left']
	cube_state_ba_c[14] = cube_ba_c['right'] + cube_ba_c['back'] + cube_ba_c['left'] + cube_ba_c['bottom'] + cube_ba_c['front'] + cube_ba_c['top']
	cube_state_ba_c[15] = cube_ba_c['bottom'] + cube_ba_c['back'] + cube_ba_c['top'] + cube_ba_c['left'] + cube_ba_c['front'] + cube_ba_c['right']
	
	cube_state_ba_c[16] = cube_ba_c['front'] + cube_ba_c['top'] + cube_ba_c['back'] + cube_ba_c['right'] + cube_ba_c['bottom'] + cube_ba_c['left']
	cube_state_ba_c[17] = cube_ba_c['front'] + cube_ba_c['left'] + cube_ba_c['back'] + cube_ba_c['top'] + cube_ba_c['right'] + cube_ba_c['bottom']
	cube_state_ba_c[18] = cube_ba_c['front'] + cube_ba_c['bottom'] + cube_ba_c['back'] + cube_ba_c['left'] + cube_ba_c['top'] + cube_ba_c['right']
	cube_state_ba_c[19] = cube_ba_c['front'] + cube_ba_c['right'] + cube_ba_c['back'] + cube_ba_c['bottom'] + cube_ba_c['left'] + cube_ba_c['top']
	
	cube_state_ba_c[20] = cube_ba_c['back'] + cube_ba_c['top'] + cube_ba_c['front'] + cube_ba_c['left'] + cube_ba_c['bottom'] + cube_ba_c['right']
	cube_state_ba_c[21] = cube_ba_c['back'] + cube_ba_c['left'] + cube_ba_c['front'] + cube_ba_c['bottom'] + cube_ba_c['right'] + cube_ba_c['top']
	cube_state_ba_c[22] = cube_ba_c['back'] + cube_ba_c['bottom'] + cube_ba_c['front'] + cube_ba_c['right'] + cube_ba_c['top'] + cube_ba_c['left']
	cube_state_ba_c[23] = cube_ba_c['back'] + cube_ba_c['right'] + cube_ba_c['front'] + cube_ba_c['top'] + cube_ba_c['left'] + cube_ba_c['bottom']
	
	cube_state_str_ba_c = [None] * 24
	for i in range(24):
		cube_state_str_ba_c[i] = ''.join(cube_state_ba_c[i])
		if cube_state_str_ba_c[i] in state:
			return

	queue.put((diff, cube_ba_c))
	state.add(cube_state_str_ba_c[0])
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
	
	# check repeated states
	cube_state_l = [None] * 24
	cube_state_l[0] = cube_l['left'] + cube_l['top'] + cube_l['right'] + cube_l['front'] + cube_l['bottom'] + cube_l['back']
	cube_state_l[1] = cube_l['bottom'] + cube_l['left'] + cube_l['top'] + cube_l['front'] + cube_l['right'] + cube_l['back']
	cube_state_l[2] = cube_l['right'] + cube_l['bottom'] + cube_l['left'] + cube_l['front'] + cube_l['top'] + cube_l['back']
	cube_state_l[3] = cube_l['top'] + cube_l['right'] + cube_l['bottom'] + cube_l['front'] + cube_l['left'] + cube_l['back']

	cube_state_l[4] = cube_l['left'] + cube_l['front'] + cube_l['right'] + cube_l['bottom'] + cube_l['back'] + cube_l['top']
	cube_state_l[5] = cube_l['bottom'] + cube_l['front'] + cube_l['top'] + cube_l['right'] + cube_l['back'] + cube_l['left']
	cube_state_l[6] = cube_l['right'] + cube_l['front'] + cube_l['left'] + cube_l['top'] + cube_l['back'] + cube_l['bottom']
	cube_state_l[7] = cube_l['top'] + cube_l['front'] + cube_l['bottom'] + cube_l['left'] + cube_l['back'] + cube_l['right']
	
	cube_state_l[8] = cube_l['left'] + cube_l['bottom'] + cube_l['right'] + cube_l['back'] + cube_l['top'] + cube_l['front']
	cube_state_l[9] = cube_l['top'] + cube_l['left'] + cube_l['bottom'] + cube_l['back'] + cube_l['right'] + cube_l['front']
	cube_state_l[10] = cube_l['right'] + cube_l['top'] + cube_l['left'] + cube_l['back'] + cube_l['bottom'] + cube_l['front']
	cube_state_l[11] = cube_l['bottom'] + cube_l['right'] + cube_l['top'] + cube_l['back'] + cube_l['left'] + cube_l['front']
	
	cube_state_l[12] = cube_l['left'] + cube_l['back'] + cube_l['right'] + cube_l['top'] + cube_l['front'] + cube_l['bottom']
	cube_state_l[13] = cube_l['top'] + cube_l['back'] + cube_l['bottom'] + cube_l['right'] + cube_l['front'] + cube_l['left']
	cube_state_l[14] = cube_l['right'] + cube_l['back'] + cube_l['left'] + cube_l['bottom'] + cube_l['front'] + cube_l['top']
	cube_state_l[15] = cube_l['bottom'] + cube_l['back'] + cube_l['top'] + cube_l['left'] + cube_l['front'] + cube_l['right']
	
	cube_state_l[16] = cube_l['front'] + cube_l['top'] + cube_l['back'] + cube_l['right'] + cube_l['bottom'] + cube_l['left']
	cube_state_l[17] = cube_l['front'] + cube_l['left'] + cube_l['back'] + cube_l['top'] + cube_l['right'] + cube_l['bottom']
	cube_state_l[18] = cube_l['front'] + cube_l['bottom'] + cube_l['back'] + cube_l['left'] + cube_l['top'] + cube_l['right']
	cube_state_l[19] = cube_l['front'] + cube_l['right'] + cube_l['back'] + cube_l['bottom'] + cube_l['left'] + cube_l['top']
	
	cube_state_l[20] = cube_l['back'] + cube_l['top'] + cube_l['front'] + cube_l['left'] + cube_l['bottom'] + cube_l['right']
	cube_state_l[21] = cube_l['back'] + cube_l['left'] + cube_l['front'] + cube_l['bottom'] + cube_l['right'] + cube_l['top']
	cube_state_l[22] = cube_l['back'] + cube_l['bottom'] + cube_l['front'] + cube_l['right'] + cube_l['top'] + cube_l['left']
	cube_state_l[23] = cube_l['back'] + cube_l['right'] + cube_l['front'] + cube_l['top'] + cube_l['left'] + cube_l['bottom']
	
	cube_state_str_l = [None] * 24
	for i in range(24):
		cube_state_str_l[i] = ''.join(cube_state_l[i])
		if cube_state_str_l[i] in state:
			return

	queue.put((diff, cube_l))
	state.add(cube_state_str_l[0])
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
	
	# check repeated states
	cube_state_l_c = [None] * 24
	cube_state_l_c[0] = cube_l_c['left'] + cube_l_c['top'] + cube_l_c['right'] + cube_l_c['front'] + cube_l_c['bottom'] + cube_l_c['back']
	cube_state_l_c[1] = cube_l_c['bottom'] + cube_l_c['left'] + cube_l_c['top'] + cube_l_c['front'] + cube_l_c['right'] + cube_l_c['back']
	cube_state_l_c[2] = cube_l_c['right'] + cube_l_c['bottom'] + cube_l_c['left'] + cube_l_c['front'] + cube_l_c['top'] + cube_l_c['back']
	cube_state_l_c[3] = cube_l_c['top'] + cube_l_c['right'] + cube_l_c['bottom'] + cube_l_c['front'] + cube_l_c['left'] + cube_l_c['back']

	cube_state_l_c[4] = cube_l_c['left'] + cube_l_c['front'] + cube_l_c['right'] + cube_l_c['bottom'] + cube_l_c['back'] + cube_l_c['top']
	cube_state_l_c[5] = cube_l_c['bottom'] + cube_l_c['front'] + cube_l_c['top'] + cube_l_c['right'] + cube_l_c['back'] + cube_l_c['left']
	cube_state_l_c[6] = cube_l_c['right'] + cube_l_c['front'] + cube_l_c['left'] + cube_l_c['top'] + cube_l_c['back'] + cube_l_c['bottom']
	cube_state_l_c[7] = cube_l_c['top'] + cube_l_c['front'] + cube_l_c['bottom'] + cube_l_c['left'] + cube_l_c['back'] + cube_l_c['right']
	
	cube_state_l_c[8] = cube_l_c['left'] + cube_l_c['bottom'] + cube_l_c['right'] + cube_l_c['back'] + cube_l_c['top'] + cube_l_c['front']
	cube_state_l_c[9] = cube_l_c['top'] + cube_l_c['left'] + cube_l_c['bottom'] + cube_l_c['back'] + cube_l_c['right'] + cube_l_c['front']
	cube_state_l_c[10] = cube_l_c['right'] + cube_l_c['top'] + cube_l_c['left'] + cube_l_c['back'] + cube_l_c['bottom'] + cube_l_c['front']
	cube_state_l_c[11] = cube_l_c['bottom'] + cube_l_c['right'] + cube_l_c['top'] + cube_l_c['back'] + cube_l_c['left'] + cube_l_c['front']
	
	cube_state_l_c[12] = cube_l_c['left'] + cube_l_c['back'] + cube_l_c['right'] + cube_l_c['top'] + cube_l_c['front'] + cube_l_c['bottom']
	cube_state_l_c[13] = cube_l_c['top'] + cube_l_c['back'] + cube_l_c['bottom'] + cube_l_c['right'] + cube_l_c['front'] + cube_l_c['left']
	cube_state_l_c[14] = cube_l_c['right'] + cube_l_c['back'] + cube_l_c['left'] + cube_l_c['bottom'] + cube_l_c['front'] + cube_l_c['top']
	cube_state_l_c[15] = cube_l_c['bottom'] + cube_l_c['back'] + cube_l_c['top'] + cube_l_c['left'] + cube_l_c['front'] + cube_l_c['right']
	
	cube_state_l_c[16] = cube_l_c['front'] + cube_l_c['top'] + cube_l_c['back'] + cube_l_c['right'] + cube_l_c['bottom'] + cube_l_c['left']
	cube_state_l_c[17] = cube_l_c['front'] + cube_l_c['left'] + cube_l_c['back'] + cube_l_c['top'] + cube_l_c['right'] + cube_l_c['bottom']
	cube_state_l_c[18] = cube_l_c['front'] + cube_l_c['bottom'] + cube_l_c['back'] + cube_l_c['left'] + cube_l_c['top'] + cube_l_c['right']
	cube_state_l_c[19] = cube_l_c['front'] + cube_l_c['right'] + cube_l_c['back'] + cube_l_c['bottom'] + cube_l_c['left'] + cube_l_c['top']
	
	cube_state_l_c[20] = cube_l_c['back'] + cube_l_c['top'] + cube_l_c['front'] + cube_l_c['left'] + cube_l_c['bottom'] + cube_l_c['right']
	cube_state_l_c[21] = cube_l_c['back'] + cube_l_c['left'] + cube_l_c['front'] + cube_l_c['bottom'] + cube_l_c['right'] + cube_l_c['top']
	cube_state_l_c[22] = cube_l_c['back'] + cube_l_c['bottom'] + cube_l_c['front'] + cube_l_c['right'] + cube_l_c['top'] + cube_l_c['left']
	cube_state_l_c[23] = cube_l_c['back'] + cube_l_c['right'] + cube_l_c['front'] + cube_l_c['top'] + cube_l_c['left'] + cube_l_c['bottom']
	
	cube_state_str_l_c = [None] * 24
	for i in range(24):
		cube_state_str_l_c[i] = ''.join(cube_state_l_c[i])
		if cube_state_str_l_c[i] in state:
			return

	queue.put((diff, cube_l_c))
	state.add(cube_state_str_l_c[0])
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
	
	# check repeated states
	cube_state_r = [None] * 24
	cube_state_r[0] = cube_r['left'] + cube_r['top'] + cube_r['right'] + cube_r['front'] + cube_r['bottom'] + cube_r['back']
	cube_state_r[1] = cube_r['bottom'] + cube_r['left'] + cube_r['top'] + cube_r['front'] + cube_r['right'] + cube_r['back']
	cube_state_r[2] = cube_r['right'] + cube_r['bottom'] + cube_r['left'] + cube_r['front'] + cube_r['top'] + cube_r['back']
	cube_state_r[3] = cube_r['top'] + cube_r['right'] + cube_r['bottom'] + cube_r['front'] + cube_r['left'] + cube_r['back']

	cube_state_r[4] = cube_r['left'] + cube_r['front'] + cube_r['right'] + cube_r['bottom'] + cube_r['back'] + cube_r['top']
	cube_state_r[5] = cube_r['bottom'] + cube_r['front'] + cube_r['top'] + cube_r['right'] + cube_r['back'] + cube_r['left']
	cube_state_r[6] = cube_r['right'] + cube_r['front'] + cube_r['left'] + cube_r['top'] + cube_r['back'] + cube_r['bottom']
	cube_state_r[7] = cube_r['top'] + cube_r['front'] + cube_r['bottom'] + cube_r['left'] + cube_r['back'] + cube_r['right']
	
	cube_state_r[8] = cube_r['left'] + cube_r['bottom'] + cube_r['right'] + cube_r['back'] + cube_r['top'] + cube_r['front']
	cube_state_r[9] = cube_r['top'] + cube_r['left'] + cube_r['bottom'] + cube_r['back'] + cube_r['right'] + cube_r['front']
	cube_state_r[10] = cube_r['right'] + cube_r['top'] + cube_r['left'] + cube_r['back'] + cube_r['bottom'] + cube_r['front']
	cube_state_r[11] = cube_r['bottom'] + cube_r['right'] + cube_r['top'] + cube_r['back'] + cube_r['left'] + cube_r['front']
	
	cube_state_r[12] = cube_r['left'] + cube_r['back'] + cube_r['right'] + cube_r['top'] + cube_r['front'] + cube_r['bottom']
	cube_state_r[13] = cube_r['top'] + cube_r['back'] + cube_r['bottom'] + cube_r['right'] + cube_r['front'] + cube_r['left']
	cube_state_r[14] = cube_r['right'] + cube_r['back'] + cube_r['left'] + cube_r['bottom'] + cube_r['front'] + cube_r['top']
	cube_state_r[15] = cube_r['bottom'] + cube_r['back'] + cube_r['top'] + cube_r['left'] + cube_r['front'] + cube_r['right']
	
	cube_state_r[16] = cube_r['front'] + cube_r['top'] + cube_r['back'] + cube_r['right'] + cube_r['bottom'] + cube_r['left']
	cube_state_r[17] = cube_r['front'] + cube_r['left'] + cube_r['back'] + cube_r['top'] + cube_r['right'] + cube_r['bottom']
	cube_state_r[18] = cube_r['front'] + cube_r['bottom'] + cube_r['back'] + cube_r['left'] + cube_r['top'] + cube_r['right']
	cube_state_r[19] = cube_r['front'] + cube_r['right'] + cube_r['back'] + cube_r['bottom'] + cube_r['left'] + cube_r['top']
	
	cube_state_r[20] = cube_r['back'] + cube_r['top'] + cube_r['front'] + cube_r['left'] + cube_r['bottom'] + cube_r['right']
	cube_state_r[21] = cube_r['back'] + cube_r['left'] + cube_r['front'] + cube_r['bottom'] + cube_r['right'] + cube_r['top']
	cube_state_r[22] = cube_r['back'] + cube_r['bottom'] + cube_r['front'] + cube_r['right'] + cube_r['top'] + cube_r['left']
	cube_state_r[23] = cube_r['back'] + cube_r['right'] + cube_r['front'] + cube_r['top'] + cube_r['left'] + cube_r['bottom']
	
	cube_state_str_r = [None] * 24
	for i in range(24):
		cube_state_str_r[i] = ''.join(cube_state_r[i])
		if cube_state_str_r[i] in state:
			return

	queue.put((diff, cube_r))
	state.add(cube_state_str_r[0])
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
	
	# check repeated states
	cube_state_r_c = [None] * 24
	cube_state_r_c[0] = cube_r_c['left'] + cube_r_c['top'] + cube_r_c['right'] + cube_r_c['front'] + cube_r_c['bottom'] + cube_r_c['back']
	cube_state_r_c[1] = cube_r_c['bottom'] + cube_r_c['left'] + cube_r_c['top'] + cube_r_c['front'] + cube_r_c['right'] + cube_r_c['back']
	cube_state_r_c[2] = cube_r_c['right'] + cube_r_c['bottom'] + cube_r_c['left'] + cube_r_c['front'] + cube_r_c['top'] + cube_r_c['back']
	cube_state_r_c[3] = cube_r_c['top'] + cube_r_c['right'] + cube_r_c['bottom'] + cube_r_c['front'] + cube_r_c['left'] + cube_r_c['back']

	cube_state_r_c[4] = cube_r_c['left'] + cube_r_c['front'] + cube_r_c['right'] + cube_r_c['bottom'] + cube_r_c['back'] + cube_r_c['top']
	cube_state_r_c[5] = cube_r_c['bottom'] + cube_r_c['front'] + cube_r_c['top'] + cube_r_c['right'] + cube_r_c['back'] + cube_r_c['left']
	cube_state_r_c[6] = cube_r_c['right'] + cube_r_c['front'] + cube_r_c['left'] + cube_r_c['top'] + cube_r_c['back'] + cube_r_c['bottom']
	cube_state_r_c[7] = cube_r_c['top'] + cube_r_c['front'] + cube_r_c['bottom'] + cube_r_c['left'] + cube_r_c['back'] + cube_r_c['right']
	
	cube_state_r_c[8] = cube_r_c['left'] + cube_r_c['bottom'] + cube_r_c['right'] + cube_r_c['back'] + cube_r_c['top'] + cube_r_c['front']
	cube_state_r_c[9] = cube_r_c['top'] + cube_r_c['left'] + cube_r_c['bottom'] + cube_r_c['back'] + cube_r_c['right'] + cube_r_c['front']
	cube_state_r_c[10] = cube_r_c['right'] + cube_r_c['top'] + cube_r_c['left'] + cube_r_c['back'] + cube_r_c['bottom'] + cube_r_c['front']
	cube_state_r_c[11] = cube_r_c['bottom'] + cube_r_c['right'] + cube_r_c['top'] + cube_r_c['back'] + cube_r_c['left'] + cube_r_c['front']
	
	cube_state_r_c[12] = cube_r_c['left'] + cube_r_c['back'] + cube_r_c['right'] + cube_r_c['top'] + cube_r_c['front'] + cube_r_c['bottom']
	cube_state_r_c[13] = cube_r_c['top'] + cube_r_c['back'] + cube_r_c['bottom'] + cube_r_c['right'] + cube_r_c['front'] + cube_r_c['left']
	cube_state_r_c[14] = cube_r_c['right'] + cube_r_c['back'] + cube_r_c['left'] + cube_r_c['bottom'] + cube_r_c['front'] + cube_r_c['top']
	cube_state_r_c[15] = cube_r_c['bottom'] + cube_r_c['back'] + cube_r_c['top'] + cube_r_c['left'] + cube_r_c['front'] + cube_r_c['right']
	
	cube_state_r_c[16] = cube_r_c['front'] + cube_r_c['top'] + cube_r_c['back'] + cube_r_c['right'] + cube_r_c['bottom'] + cube_r_c['left']
	cube_state_r_c[17] = cube_r_c['front'] + cube_r_c['left'] + cube_r_c['back'] + cube_r_c['top'] + cube_r_c['right'] + cube_r_c['bottom']
	cube_state_r_c[18] = cube_r_c['front'] + cube_r_c['bottom'] + cube_r_c['back'] + cube_r_c['left'] + cube_r_c['top'] + cube_r_c['right']
	cube_state_r_c[19] = cube_r_c['front'] + cube_r_c['right'] + cube_r_c['back'] + cube_r_c['bottom'] + cube_r_c['left'] + cube_r_c['top']
	
	cube_state_r_c[20] = cube_r_c['back'] + cube_r_c['top'] + cube_r_c['front'] + cube_r_c['left'] + cube_r_c['bottom'] + cube_r_c['right']
	cube_state_r_c[21] = cube_r_c['back'] + cube_r_c['left'] + cube_r_c['front'] + cube_r_c['bottom'] + cube_r_c['right'] + cube_r_c['top']
	cube_state_r_c[22] = cube_r_c['back'] + cube_r_c['bottom'] + cube_r_c['front'] + cube_r_c['right'] + cube_r_c['top'] + cube_r_c['left']
	cube_state_r_c[23] = cube_r_c['back'] + cube_r_c['right'] + cube_r_c['front'] + cube_r_c['top'] + cube_r_c['left'] + cube_r_c['bottom']
	
	cube_state_str_r_c = [None] * 24
	for i in range(24):
		cube_state_str_r_c[i] = ''.join(cube_state_r_c[i])
		if cube_state_str_r_c[i] in state:
			return

	queue.put((diff, cube_r_c))
	state.add(cube_state_str_r_c[0])
	# print(cube_r_c['path'])


def solveCube(name):
	with open(name) as file:
		start = time()
		rubik = [[str(char) for char in line.strip()] for line in file]
		left = [rubik[0][0],rubik[0][2],rubik[1][0],rubik[1][2]]
		top = [rubik[0][4],rubik[0][6],rubik[1][4],rubik[1][6]]
		right = [rubik[0][8],rubik[0][10],rubik[1][8],rubik[1][10]]
		front = [rubik[2][0],rubik[2][2],rubik[3][0],rubik[3][2]]
		bottom = [rubik[4][0],rubik[4][2],rubik[5][0],rubik[5][2]]
		back = [rubik[6][0],rubik[6][2],rubik[7][0],rubik[7][2]]
		path = []
		cube_list = []
		cube_list = left + top + right + front + bottom + back
		cube_state = ''.join(cube_list)
		# print cube_state
		state.add(cube_state)
		diff = heuristic(cube_list)
		cube_input = {'top':top, 'bottom':bottom, 'front':front, 'back':back, 'left':left, 'right':right, 'path':path}
		queue.put((diff, cube_input))
		cost = 0

		# for i in range(5):
		# if queue:
		while queue:
			cube_cur = queue.get()[1]
			cost += 1
			if cube_cur['top'].count(cube_cur['top'][0]) == len(cube_cur['top']):
				if cube_cur['bottom'].count(cube_cur['bottom'][0]) == len(cube_cur['bottom']):
					if cube_cur['left'].count(cube_cur['left'][0]) == len(cube_cur['left']):
						if cube_cur['right'].count(cube_cur['right'][0]) == len(cube_cur['right']):
							if cube_cur['front'].count(cube_cur['front'][0]) == len(cube_cur['front']):
								if cube_cur['back'].count(cube_cur['back'][0]) == len(cube_cur['back']):
									print 'File Name: {}'.format(name)
									print 'Solution:  {}'.format(''.join(cube_cur['path']))
									print 'Cost:      {} nodes expanded.'.format(cost)
									print 'Run Time:  {} seconds'.format(time() - start)
									print '\n'
									break

			rotate_top_cw(cube_cur)
			rotate_top_ccw(cube_cur)
			rotate_right_cw(cube_cur)
			rotate_right_ccw(cube_cur)
			rotate_front_cw(cube_cur)
			rotate_front_ccw(cube_cur)
			# rotate_bottom_cw(cube_cur)
			# rotate_bottom_ccw(cube_cur)
			# rotate_left_cw(cube_cur)
			# rotate_left_ccw(cube_cur)
			# rotate_back_cw(cube_cur)
			# rotate_back_ccw(cube_cur)

# solveCube('goal.txt')
# solveCube('cube.txt')
# solveCube('cube1_1.txt')
# solveCube('cube1_2.txt')
# solveCube('cube1_3.txt')
# solveCube('cube2_1.txt')
# solveCube('cube2_2.txt')
# solveCube('cube2_3.txt')
solveCube('cube3_1.txt')
