

def readData(name):
	occurrences = []
	wordCount = [0] * 40
	uniqueWord = set()
	for i in range(40):
		occurrences.append({})
	with open(name, 'r') as file:
		for line in file:
			review = line.strip().split(' ')
			# map class -1,1 to 0,1
			priori = int(review[0])
			for word in review[1:]:
				word = word.split(':')
				if word[0] not in occurrences[priori]:
					occurrences[priori][word[0]] = 0
				occurrences[priori][word[0]] += int(word[1])
				wordCount[priori] += int(word[1])
				uniqueWord.add(word[0])
	return occurrences, wordCount, uniqueWord


def findLikelihood(occurrences, wordCount, uniqueWord):
	likehood = []
	for i in range(40):
		likehood.append({})
		V = len(uniqueWord)
		for word in uniqueWord:
			for j in range(40):
				if word not in occurrences[i]:
					likehood[i][word] = float(1) / float(wordCount[i] + V)		
				else:
					likehood[i][word] = float(1 + occurrences[i][word]) / float(wordCount[i] + V)
	return likehood


def findPrior(wordCount):
	prior = []
	total = 0
	for i in range(40):
		total += wordCount[i]
	for i in range(40):
		possibility = float(wordCount[i])/total
		prior.append(possibility)
	return prior

def trainingTopicMultinominal(name):
	occurrences, wordCount, uniqueWord = readData(name)
	likehood = findLikelihood(occurrences, wordCount, uniqueWord)
	prior = findPrior(wordCount)
	return likehood, prior