import numpy as np
import math
import random
from matplotlib import pyplot as plt

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


def shuffle(order):
	random.shuffle(order)
	return order


def training(epoch,bias,randomize,shuf,alpha):
	trainingImage=readimage('trainingimages')
	trainingLabel=readlabel('traininglabels')
	num_instance = len(trainingLabel)
	num_feature = len(trainingImage[0])
	num_class= 10

	if bias:
		num_feature+=1
		trainingImage=np.insert(trainingImage,0,1,axis=1)

	if randomize:
		Weight=np.random.rand(epoch,num_class,num_feature)
	else:
		Weight=np.zeros((epoch,num_class,num_feature))

	accy=[]
	idx=[]
	for ep in range(1,epoch):
		Miss=np.ones(num_instance)
		Weight[ep]=Weight[ep-1]
		if shuf:
			for instance in shuffle([i for i in range(num_instance)]):
				result=[]
				for cla in range(num_class):
					result.append(np.sum(np.multiply(Weight[ep,cla],trainingImage[instance])))
			
				prediction=result.index(max(result))
				truth=int(trainingLabel[instance])

				if truth==prediction:
					Miss[instance]=0
				else:
					mult= np.multiply(trainingImage[instance],alpha/(alpha+ float(ep)))
					Weight[ep,prediction]= np.subtract(Weight[ep,prediction],mult)
					Weight[ep,truth]=np.add(Weight[ep,truth],mult)

			print('ep:',ep,' accy: ', 1-np.sum(Miss)/num_instance)
			accy.append(1-np.sum(Miss)/num_instance)
			idx.append(ep)
		else:
			for instance in range(num_instance):
				result=[]
				for cla in range(num_class):
					result.append(np.sum(np.multiply(Weight[ep,cla],trainingImage[instance])))
			
				prediction=result.index(max(result))
				truth=int(trainingLabel[instance])

				if truth==prediction:
					Miss[instance]=0
				else:
					mult= np.multiply(trainingImage[instance],alpha/(alpha+ float(ep)))
					Weight[ep,prediction]= np.subtract(Weight[ep,prediction],mult)
					Weight[ep,truth]=np.add(Weight[ep,truth],mult)

			print('ep:',ep,' accy: ', 1-np.sum(Miss)/num_instance)
			
			accy.append(1-np.sum(Miss)/num_instance)
			idx.append(ep)
	plt.plot(idx,accy)
	plt.ylabel('accuracy per epoch')
	plt.xlabel('epoch')
	plt.title('Training Curve')
	plt.axis([0,epoch,0,1])
	plt.show()

	return Weight[epoch-1]


def analyze(TestList,testingLabel):
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
			string+=str(round(col,2))+' '
		print(string)

	return accuracyCount/1000.0


def testing(epoch,bias,randomize,shuf,alpha):
	testingImage=readimage('testimages')
	testingLabel=readlabel('testlabels')
	num_class=10
	Weight=training(epoch,bias,randomize,shuf,alpha)
	np.set_printoptions(threshold=np.nan)
	print(Weight[0].shape)
	plt.imshow(np.reshape(Weight[0],(28,28)),interpolation='nearest')
	plt.show()

	if bias:
		testingImage=np.insert(testingImage,0,1,axis=1)

	prediction=[]
	for instance in range(len(testingLabel)):
		result=[]
		for cla in range(num_class):
			result.append(np.sum(np.multiply(Weight[cla],testingImage[instance])))
		prediction.append(result.index(max(result)))

	analyze(prediction,testingLabel)
		
testing(100,False,True,True,100)


