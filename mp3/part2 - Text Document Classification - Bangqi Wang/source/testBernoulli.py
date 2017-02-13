import math
import numpy as np

def calculateClass(words, likehood, prior):
	estimate = []
	for i in range(2):
		estimate.append(math.log(prior[i]))
	for word in words:
		word = word.split(':')
		if word[0] in likehood[0]:
			for i in range(int(word[1])):
				# calculate negative
				estimate[0] += math.log(likehood[0][word[0]])
		if word[0] in likehood[1]:
			for i in range(int(word[1])):
				# calculate negative
				estimate[1] += math.log(likehood[1][word[0]])
	return 0 if estimate[0] > estimate[1] else 1

def calculateConfusi(matrix):
	for i in matrix:
		total = float(np.sum(i))
		for j in range(2):
			i[j] = float(i[j])/total
	return matrix

def testingBernoulli(name, likehood, prior):
	predict = {}
	predict[True] = 0
	predict[False] = 0
	confusiMatrix = np.zeros((2,2))
	with open(name, 'r') as file:
		for line in file:
			review = line.strip().split(' ')
			label = int(int(review[0]) * 0.5 + 0.5)
			pred = calculateClass(review[1:], likehood, prior)
			confusiMatrix[label][pred] += 1
			predict[label==pred] += 1
		confusiMatrix = calculateConfusi(confusiMatrix)
	return float(predict[True]) / float(predict[True] + predict[False]), confusiMatrix
