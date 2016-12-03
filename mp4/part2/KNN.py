import numpy as np
import math
import random
import operator
import scipy.spatial.distance as dist

def readimage(imagefile):
	imageset=[]
	countLine=0
	image=[]
	with open(imagefile,'r') as infile:
		for line in infile:
			if countLine==28:
				imageset.append(image)
				image=[]
				countLine=0
			countLine+=1
			temp=list(line)
			image.append(temp[:28])
	imageset.append(image)

	retImageset=[]
	for img in imageset:
		retImage=[]
		for line in img:
			for i in line:
				if i==' ':
					retImage.append(0)
				else:
					retImage.append(1)
		retImageset.append(retImage)		
	return np.array(retImageset)


def readlabel(labelfile):
	labelset=[]
	with open(labelfile,'r') as infile:
		for line in infile:
			labelset.append(list(line)[0])
	return np.array(labelset)


def distance(training,testing):
	return dist.hamming(testing,training)

def getvote(neighbor,trainingLabel):
	classvote={}
	for i in range(len(neighbor)):
		response=trainingLabel[neighbor[i][0]]
		#print(response)
		if response in classvote:
			classvote[response]+=1
		else:
			classvote[response]=1
	result=sorted(classvote.items(),key=operator.itemgetter(1),reverse=True)
	return result[0][0]


def analyze(TestList,testingLabel):
	#overall accuracy
	accuracyCount=0
	for i in range(0,1000):
		if int(TestList[i])==int(testingLabel[i]):
			accuracyCount+=1
	print('Overall: '+ str(accuracyCount/1000.0))

	# classification rate per digit
	classificationList=[]
	for i in range(0,10):
		classificationRate=0.0
		classcount=0
		for img in range(0,1000):
			if i == int(testingLabel[img]):
				classcount+=1
				if i == int(TestList[img]):
					classificationRate+=1
		print('Classification rate for digit '+str(i)+': '+str(round(classificationRate/classcount,3)))
		classificationList.append(classificationRate)
	
	# confusion matrix
	print('----Confusion Matrix----')
	confusionMatrix=[]
	for i in range(0,10): #truth row
		colList=[]
		for j in range(0,10): #prediction col
			classcount=0
			confusion=0
			for img in range(0,1000):
				if i == int(testingLabel[img]):
					classcount+=1
				if int(TestList[img]) == j and int(testingLabel[img])== i:
					confusion+=1
			colList.append(round(confusion/float(classcount),3))
		confusionMatrix.append(colList)
	
	for row in confusionMatrix:
		string=''
		for col in row:
			string+=str(col)+' '
		print(string)

def KNN_classifer(k):
	trainingImage=readimage('trainingimages')
	trainingLabel=readlabel('traininglabels')
	testingImage=readimage('testimages')
	testingLabel=readlabel('testlabels')
	num_instance = len(trainingLabel)
	num_feature = len(trainingImage[0])
	num_class= 10

	prediction=[]

	for i in range(len(testingLabel)):
		nearestNeighbors={}
		for j in range(len(trainingLabel)):
			nearestNeighbors[j]=distance(trainingImage[j],testingImage[i])

		nearestNeighbors=sorted(nearestNeighbors.items(),key=operator.itemgetter(1))
		vote=getvote(list(nearestNeighbors[:k]),trainingLabel)
		prediction.append(vote)
	
	analyze(prediction,testingLabel)

KNN_classifer(6)




