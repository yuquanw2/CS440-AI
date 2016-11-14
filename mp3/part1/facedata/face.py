import math
from matplotlib import pyplot as plt
import numpy as np

def readimage(imagefile):
	imageset=[]
	countLine=0
	image=[]
	with open(imagefile,'r') as infile:
		for line in infile:
			if countLine==70:
				imageset.append(image)	
				image=[]
				countLine=0
			countLine+=1
			temp=list(line)
			image.append(temp[:60])
	imageset.append(image)
	return imageset

def readlabel(labelfile):
	labelset=[]
	with open(labelfile,'r') as infile:
		for line in infile:
			labelset.append(list(line)[0])
	return labelset

def likelihoods(imageset,labelset,freq):
	Plist=[]
	laplace=1
	for digit in range(0,2):
		examplecount=freq[str(digit)]
		
		rowList=[]
		for i in range(0,70):	
			colList=[]
			for j in range(0,60):
				
				pixelcount=0
				for img in range(0,451):
					if imageset[img][i][j]!=' ' and int(labelset[img])==digit:
						pixelcount+=1
				colList.append(round((pixelcount+laplace)/float(examplecount+laplace*2),3))
			rowList.append(colList)
		Plist.append(rowList)
	return Plist

def prior(labelset):
	PriorDict={}
	for label in labelset:
		if label not in PriorDict.keys():
			PriorDict[label] = 1
		else:
			PriorDict[label] += 1
	return PriorDict


def training():
	trainingImage=readimage('facedatatrain')
	trainingLabel=readlabel('facedatatrainlabels')
	#prior
	Pdict=prior(trainingLabel)
	#likelihoods
	Plist=likelihoods(trainingImage,trainingLabel,Pdict)
	return Plist, Pdict


def testing():
	print('----start training----')
	likelihood,Prior=training()
	print('----start testing----')
	testingImage=readimage('facedatatest')
	testingLabel=readlabel('facedatatestlabels')
	
	TestList=[] # results for 150 images
	idx=0
	Prototypical= []
	for image in testingImage:
		MAP=[]
		for cla in range(0,2):
			result=0
			result+=math.log(Prior[str(cla)]/150.0)
			for i in range(0,70):
				for j in range(0,60):
					if image[i][j]!=' ':
						result += math.log(likelihood[cla][i][j])
					else:
						result += math.log(1-likelihood[cla][i][j]) ## check
			MAP.append(round(result,3))
		prediction= MAP.index(max(MAP))
		Prototypical.append((max(MAP),idx))
		TestList.append(prediction)
		idx+=1

## Analysis

	#overall accuracy
	accuracyCount=0
	for i in range(0,150):
		if TestList[i]==int(testingLabel[i]):
			accuracyCount+=1
	print('Overall: '+ str(accuracyCount/150.0))

	# classification rate per digit
	classificationList=[]
	for i in range(0,2):
		classificationRate=0.0
		classcount=0
		for img in range(0,150):
			if i == int(testingLabel[img]):
				classcount+=1
				if i == TestList[img]:
					classificationRate+=1
		if i==0:
			print('Classification rate for not face: '+str(round(classificationRate/classcount,3)))
		else:
			print('Classification rate for face: '+str(round(classificationRate/classcount,3)))
		classificationList.append(classificationRate)


testing()

