import numpy as np


def readData(name):
	likelihood = []
	for i in range(2):
		diction = {}
		likelihood.append(diction)
	with open(name, 'r') as file:
		for line in file:
			review = line.strip().split(' ')
			# map class -1,1 to 0,1
			priori = review[0] * 0.5 + 0.5
			for word in review[1:]:
				word = word.split(':')
				if word[0] not in likelihood[priori]:
					likelihood[priori][word[0]] = 0
				likelihood[priori[word[0]]] += int(word[1])
	print likelihood





def movieReview():
	likelihood = readData('rt-train.txt')




if __name__ == '__main__':
	movieReview()