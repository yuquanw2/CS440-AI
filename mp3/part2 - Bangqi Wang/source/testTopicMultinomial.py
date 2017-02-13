import math
import numpy as np

def calculateClass(words, likehood, prior):
	estimate = []
	for i in range(40):
		estimate.append(math.log(prior[i]))
	for word in words:
		word = word.split(':')
		for i in range(40):
			if word[0] in likehood[i]:
				estimate[i] += int(word[1]) * math.log(likehood[i][word[0]])
	return estimate.index(max(estimate))


def calculateConfusi(matrix):
	for i in matrix:
		total = float(np.sum(i))
		for j in range(40):
			i[j] = float(i[j])/total
	return matrix

def testingTopicMultinominal(name, likehood, prior):
	predict = {}
	predict[True] = 0
	predict[False] = 0
	confusiMatrix = np.zeros((40,40))
	with open(name, 'r') as file:
		for line in file:
			review = line.strip().split(' ')
			label = int(review[0])
			pred = calculateClass(review[1:], likehood, prior)
			confusiMatrix[label][pred] += 1
			predict[label==pred] += 1
		confusiMatrix = calculateConfusi(confusiMatrix)
	return float(predict[True]) / float(predict[True] + predict[False]), confusiMatrix