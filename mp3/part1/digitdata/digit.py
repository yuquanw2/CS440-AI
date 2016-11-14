import math
from matplotlib import pyplot as plt
import numpy as np

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
	for digit in range(0,10):
		examplecount=freq[str(digit)]
		
		rowList=[]
		for i in range(0,28):	
			colList=[]
			for j in range(0,28):
				
				pixelcount=0
				for img in range(0,5000):
					if imageset[img][i][j]!=' ' and int(labelset[img])==digit:
						pixelcount+=1
					#if imageset[img][i][j]=='#' and int(labelset[img])==digit:
					#	pixelcount+=1
					#elif imageset[img][i][j]=='+' and int(labelset[img])==digit:
					#	pixelcount+=0.5	
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
	trainingImage=readimage('trainingimages')
	trainingLabel=readlabel('traininglabels')
	#prior
	Pdict=prior(trainingLabel)
	#likelihoods
	Plist=likelihoods(trainingImage,trainingLabel,Pdict)
	return Plist, Pdict


def testing():
	print('----start training----')
	likelihood,Prior=training()
	print('----start testing----')
	testingImage=readimage('testimages')
	testingLabel=readlabel('testlabels')
	
	TestList=[] # results for 5000 images
	idx=0
	Prototypical= []
	for image in testingImage:
		MAP=[]
		for cla in range(0,10):
			result=0
			result+=math.log(Prior[str(cla)]/5000.0)
			for i in range(0,28):
				for j in range(0,28):
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
	for i in range(0,1000):
		if TestList[i]==int(testingLabel[i]):
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
				if i == TestList[img]:
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
				if TestList[img] == j and int(testingLabel[img])== i:
					confusion+=1
			colList.append(round(confusion/float(classcount),3))
		confusionMatrix.append(colList)
	
	for row in confusionMatrix:
		string=''
		for col in row:
			string+=str(col)+' '
		print(string)

	#prototypical instance
	DigitInstance=[]
	for cla in range(0,10):
		Instance=[]
		for img in range(0,1000):
			if int(testingLabel[img])==cla and TestList[img]==cla:
				Instance.append(Prototypical[img])
		largest=max(Instance)
		smallest=min(Instance)
		print('-----Prototypical instance for digit '+ str(cla)+'------')
		print('largest: ',largest)
		printDigit(testingImage[largest[1]])
		print('smallest: ',smallest)
		printDigit(testingImage[smallest[1]])
		DigitInstance.append(Instance)

	#odd ratio
	# 0.168 (4,9) 0.13 (5,3) 0,132 (7,9) 0.136 (8,3)
	drawOddRatio(likelihood,4,9)
	drawOddRatio(likelihood,5,3)
	drawOddRatio(likelihood,7,9)
	drawOddRatio(likelihood,8,3)


def printDigit(digit):
	for row in digit:
		string=''
		for col in row:
			string+= str(col)
		print(string)


def drawOddRatio(likelihood, digit1,digit2):
	#digit 1 is prediction digit 2 is truth
	plot1=np.asarray(likelihood[digit1])
	plt.imshow(plot1,interpolation='nearest')
	plt.show()
	plot2=np.asarray(likelihood[digit2])
	plt.imshow(plot2,interpolation='nearest')
	plt.show()

	OddRatio=[]
	for row in range(0,28):
		temp=[]
		for col in range(0,28):
			temp.append(math.log(likelihood[digit1][row][col]/likelihood[digit2][row][col]))
		OddRatio.append(temp)
	OddRatio=np.asarray(OddRatio)
	plt.imshow(OddRatio,interpolation='nearest')
	plt.show()
	return OddRatio

testing()
