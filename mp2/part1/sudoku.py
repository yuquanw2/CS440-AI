import sys
import copy
count=0
def readfile(grid,bank):
	sudoku=[]
	Wordbank=[]
	with open(grid,'r') as grid, open(bank,'r') as bank:
		sudoku=[[text for text in line.strip()] for line in grid]
		Wordbank=[line.strip('\r\n') for line in bank]
	return sudoku,Wordbank

def find_empty_location(sudoku):
	for row in range(len(sudoku)):
		for col in range(len(sudoku[0])):
			if sudoku[col][row]=='_':
				return True
	return False

def select_unassigned_variable(wordbank):
	longest=''
	longest_len=0
	for word in wordbank:
		if len(word) > longest_len:
			longest_len=len(word)
			longest=word
	return longest

def order_domain_value(sudoku,curr_word):
	available_list=[]
	for row in range(len(sudoku)):
		for col in range(len(sudoku[0])):
			if sudoku[row][col]=='_' or sudoku[row][col]==curr_word[0]:
				available_list.append((col,row))
	return available_list

def horizontal_check(sudoku,curr_word,value):
	if value[0]+len(curr_word)> 9:
		return False
	for i in range(len(curr_word)):
		if sudoku[value[1]][value[0]+i]!='_':
			if sudoku[value[1]][value[0]+i]!=curr_word[i]:
				return False
	#print 'horizontal check true'
	return True

def vertical_check(sudoku,curr_word,value):
	if value[1]+len(curr_word)> 9:
		#print value[1]+len(curr_word)
		return False
	for i in range(len(curr_word)):
		#print sudoku[value[1]+i][value[0]], curr_word[i]
		if sudoku[value[1]+i][value[0]]!='_':
			if sudoku[value[1]+i][value[0]]!=curr_word[i]:
				return False
	#print 'vertical check true'
	return True

def horizontal_constraint_satisfied(sudoku,row,col,word):
	for i in range(len(word)):
		#print '(',row,',',col+i,')' 
		if used_in_row(sudoku,row,col+i,word[i]) or used_in_col(sudoku,row,col+i,word[i]) or used_in_box(sudoku,row,col+i,word[i]):
			return False
	#print 'horizontal satisfied'
	return True

def vertical_constraint_satisfied(sudoku,row,col,word):
	for i in range(len(word)):
		#print word[i]
		if used_in_row(sudoku,row+i,col,word[i]) or used_in_col(sudoku,row+i,col,word[i]) or used_in_box(sudoku,row+i,col,word[i]):
			return False
	#print 'vertical satisfied'
	return True

def used_in_col(sudoku,row,col,char):
	#print 'used_in_col'
	for i in range(9):
		if i!=row and sudoku[i][col]== char:
			return True
	return False

def used_in_row(sudoku,row,col,char):
	#print 'used_in_row'
	for i in range(9):
		if i!=col and sudoku[row][i]== char:
			return True
	return False

def used_in_box(sudoku,row,col,char):
	#print 'used_in_box'
	for i in range(3):
		for j in range(3):
			if (3*(row/3)+i)!= row and (3*(col/3)+j)!= col and sudoku[3*(row/3)+i][3*(col/3)+j] == char:
				return True
	return False

def sudokuSolver(sudoku,wordbank,assignment):
	if not find_empty_location(sudoku):
		for i in range(len(assignment)):
			print assignment[i]
			#print count
		print_sudoku(sudoku)
		return True
		global count
	curr_word = select_unassigned_variable(wordbank).upper()
	#print 'curr_word: ',curr_word
	#print order_domain_value(sudoku,curr_word)
	for value in order_domain_value(sudoku,curr_word):
		#first horizontal then vertical
		#print value
		if vertical_check(sudoku,curr_word,value) and vertical_constraint_satisfied(sudoku,value[1],value[0],curr_word):
			tempsudoku = copy.deepcopy(sudoku)
		 	for i in range(len(curr_word)):
				sudoku[value[1]+i][value[0]] = curr_word[i]
			temp=''
			temp +='V,'+str(value[0]) +','+ str(value[1]) + ': ' + curr_word
			assignment.append(temp)
			tempwordbank=copy.deepcopy(wordbank)
			#print 'vertical:',curr_word
			wordbank.remove(curr_word.lower())
			#print_sudoku(sudoku)
			count+=1
			if sudokuSolver(sudoku,wordbank,assignment):
				return True
			else:
				assignment.remove(temp)
				sudoku=copy.deepcopy(tempsudoku)
				wordbank=copy.deepcopy(tempwordbank)
				##print_sudoku(sudoku)
		if horizontal_check(sudoku,curr_word,value) and horizontal_constraint_satisfied(sudoku,value[1],value[0],curr_word):
			tempsudoku = copy.deepcopy(sudoku)
			#print 'reach horizontal'
		 	for i in range(len(curr_word)):
				sudoku[value[1]][value[0]+i] = curr_word[i]
			temp=''
			temp +='H,'+str(value[0]) +','+ str(value[1]) + ': ' + curr_word
			assignment.append(temp)
			tempwordbank=copy.deepcopy(wordbank)
			#print 'horizontal: ',curr_word
			#print wordbank
			wordbank.remove(curr_word.lower())
			#print_sudoku(sudoku)
			#print 'to next level'
			count+=1
			if sudokuSolver(sudoku,wordbank,assignment):
				return True
			else:
				#print 'horizontal backprop'
				#print 'prop: ',curr_word 
				assignment.remove(temp)
				sudoku=copy.deepcopy(tempsudoku)
				wordbank=copy.deepcopy(tempwordbank)
				#print_sudoku(sudoku)
				#print wordbank
	#print 'return to last level'
	return False



def sudokuSolver_extra(sudoku,wordbank,assignment,assignment_set):
	if not find_empty_location(sudoku):
		assignment_set.append(assignment)
		#for i in range(len(assignment)):
			#print assignment[i]
			#print count
	curr_word = select_unassigned_variable(wordbank).upper()
	print 'curr_word: ',curr_word
	print wordbank
	#print order_domain_value(sudoku,curr_word)
	for value in order_domain_value(sudoku,curr_word):
		#first horizontal then vertical
		#print value
		if vertical_check(sudoku,curr_word,value) and vertical_constraint_satisfied(sudoku,value[1],value[0],curr_word):
			tempsudoku = copy.deepcopy(sudoku)
		 	for i in range(len(curr_word)):
				sudoku[value[1]+i][value[0]] = curr_word[i]
			temp=''
			temp +='V,'+str(value[0]) +','+ str(value[1]) + ': ' + curr_word
			assignment.append(temp)
			tempwordbank=copy.deepcopy(wordbank)
			wordbank.remove(curr_word.lower())
			if sudokuSolver_extra(sudoku,wordbank,assignment,assignment_set):
				return True
			else:
				assignment.remove(temp)
				sudoku=copy.deepcopy(tempsudoku)
				wordbank=copy.deepcopy(tempwordbank)
				print_sudoku(sudoku)
		if horizontal_check(sudoku,curr_word,value) and horizontal_constraint_satisfied(sudoku,value[1],value[0],curr_word):
			
			tempsudoku = copy.deepcopy(sudoku)
		 	for i in range(len(curr_word)):
				sudoku[value[1]][value[0]+i] = curr_word[i]
			temp=''
			temp +='H,'+str(value[0]) +','+ str(value[1]) + ': ' + curr_word
			assignment.append(temp)
			tempwordbank=copy.deepcopy(wordbank)
			wordbank.remove(curr_word.lower())
			if sudokuSolver_extra(sudoku,wordbank,assignment,assignment_set):
				return True
			else: 
				assignment.remove(temp)
				sudoku=copy.deepcopy(tempsudoku)
				wordbank=copy.deepcopy(tempwordbank)
				print_sudoku(sudoku)
	wordbank.remove(curr_word.lower())
	return sudokuSolver_extra(sudoku,wordbank,assignment,assignment_set)

	

def print_sudoku(sudoku):
	for i, line in enumerate(sudoku):
		string=''
		for j, char in enumerate(line):
			string+=char
		print string
def main():
	if len(sys.argv)<3:
		sys.stderr.write("Expecting: Grid Wordbank")
		sys.exit(1)
	grid,bank = sys.argv[1], sys.argv[2]
	sudoku,wordbank=readfile(grid,bank)
	assignment=[]
	assignment_set=[]
	sudokuSolver(sudoku,wordbank,assignment)
	global count
	print 'Number of node Expanded without leaves:',count
	#print assignment_set
	#sudokuSolver_extra(sudoku,wordbank,assignment,assignment_set)
	
if __name__ =='__main__':
	main()