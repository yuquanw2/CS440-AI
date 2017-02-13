import numpy as np
import math
from trainMultinomial import *
from testMultinomial import *
from trainBernoulli import *
from testBernoulli import *
from trainTopicBernoulli import *
from testTopicMultinomial import *
from trainTopicMultinomial import *
from testTopicBernoulli import *



def movieReviewMultinomial():
	likehood, prior, odds, like = trainingMultinominal('movie_review/rt-train.txt')
	accuracy, confusiMatrix = testingMultinominal('movie_review/rt-test.txt', likehood, prior)
	return accuracy, confusiMatrix, odds, like


def conversationMultinomial():
	likehood, prior, odds, like = trainingMultinominal('fisher_2topic/fisher_train_2topic.txt')
	accuracy, confusiMatrix = testingMultinominal('fisher_2topic/fisher_test_2topic.txt', likehood, prior)
	return accuracy, confusiMatrix, odds, like


def movieReviewBernoulli():
	likehood, prior, odds, like = trainingBernoulli('movie_review/rt-train.txt')
	accuracy, confusiMatrix = testingBernoulli('movie_review/rt-test.txt', likehood, prior)
	return accuracy, confusiMatrix, odds, like


def conversationBernoulli():
	likehood, prior, odds, like = trainingBernoulli('fisher_2topic/fisher_train_2topic.txt')
	accuracy, confusiMatrix = testingBernoulli('fisher_2topic/fisher_test_2topic.txt', likehood, prior)
	return accuracy, confusiMatrix, odds, like


def topicsMultinomial():
	likehood, prior = trainingTopicMultinominal('fisher_40topic/fisher_train_40topic.txt')
	accuracy, confusiMatrix = testingTopicMultinominal('fisher_40topic/fisher_test_40topic.txt', likehood, prior)
	return accuracy, confusiMatrix

def topicsBernoulli():
	likehood, prior = trainingTopicBernoulli('fisher_40topic/fisher_train_40topic.txt')
	accuracy, confusiMatrix = testingTopicBernoulli('fisher_40topic/fisher_test_40topic.txt', likehood, prior)
	return accuracy, confusiMatrix


if __name__ == '__main__':
	# ret = movieReviewMultinomial()
	# print 'The accuracy is {} for Movie Review with Multinomial Model.\nConfusion Matrix:\n{}'.format(ret[0], ret[1])

	# ret = conversationMultinomial()
	# print 'The accuracy is {} for Conversation with Multinomial Model.\nConfusion Matrix:\n{}'.format(ret[0], ret[1])	
	
	# ret = movieReviewBernoulli()
	# print 'The accuracy is {} for Movie Review with Bernoulli Model.\nConfusion Matrix:\n{}'.format(ret[0], ret[1])
	
	# ret = conversationBernoulli()
	# print 'The accuracy is {} for Conversation with Bernoulli Model.\nConfusion Matrix:\n{}'.format(ret[0], ret[1])	
	
	# print 'The accuracy is {} for Topics with Multinomial Model.'.format(round(topicsMultinomial(), 4))
	# print 'The accuracy is {} for Topics with Bernoulli Model.'.format(round(topicsBernoulli(), 4))

	# print 'The confusion matrix is {}'.format(ret[2])

	# with open('output.csv', 'w+') as file:
	# 	ret1 = topicsMultinomial()
	# 	print np.array(ret1[1])
	# 	for item in ret1[1]:
	# 		file.write(','.join([str(round(x,4)) for x in item]) + '\n')
	# 	file.write('\n')
	# 	ret2 = topicsBernoulli()
	# 	print np.array(ret2[1])
	# 	for item in ret2[1]:
	# 		file.write(','.join([str(round(x,4)) for x in item]) + '\n')

	with open('output.csv','r') as file:
		with open('confusion.csv','w+') as confusionFile:
			count = 0
			percentage = []
			for i in range(2):
				percentage.append([])
			model = 0
			for line in file:
				if line == '\n':
					model += 1
					count = 0
					continue
				record = line.strip().split(',')
				record = [float(x) for x in record]
				
				output = []
				output.append(str(int(count)))
				output.append(str(round(max(record),4)))
				output.append(str(int(record.index(sorted(record)[-2]))))
				output.append(str(round(sorted(record)[-2],4)))
				output = ','.join(output)
				percentage[model].append(output)
				count += 1
			multinomial = '\n'.join(percentage[0])
			confusionFile.write(multinomial)
			confusionFile.write('\n\n')
			bernoulli = '\n'.join(percentage[1])
			confusionFile.write(bernoulli)

			# ret2 = topicsBernoulli()
			# for i in range(40):
			# 	confusionFile.write(str(i) + ',' + str(round(max(ret2[1][i]),4)) + ',' + str(ret2[i].index(sorted(ret2[i])[-2])) + ',' + str(round(sorted(ret2[i])[-2], 4)) + '\n')
		