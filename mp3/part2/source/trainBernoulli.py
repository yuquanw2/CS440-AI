

def readData(name):
	occurrences = []
	wordCount = [0] * 2
	uniqueWord = set()
	for i in range(2):
		occurrences.append({})
	with open(name, 'r') as file:
		for line in file:
			review = line.strip().split(' ')
			# map class -1,1 to 0,1
			priori = int(int(review[0]) * 0.5 + 0.5)
			for word in review[1:]:
				word = word.split(':')
				if word[0] not in occurrences[priori]:
					occurrences[priori][word[0]] = 0
					wordCount[priori] += 1
				occurrences[priori][word[0]] += 1
				uniqueWord.add(word[0])
	return occurrences, wordCount, uniqueWord


def findLikelihood(occurrences, wordCount, uniqueWord):
	likehood = []
	for i in range(2):
		likehood.append({})
		V = 2
		for word in uniqueWord:
			for j in range(2):
				if word not in occurrences[i]:
					likehood[i][word] = float(1) / float(wordCount[i] + V)		
				else:
					likehood[i][word] = float(1 + occurrences[i][word]) / float(wordCount[i] + V)
	return likehood


def findOdds(uniqueWord, likehood):
	odds = []
	for i in range(2):
		odds.append([])
	for word in uniqueWord:
		for i in range(2):
			odds[i].append((likehood[i][word]/likehood[1-i][word], word))
	for i in range(2):
		odds[i] = sorted(odds[i])[::-1][:10]
	return odds


def findlike(uniqueWord, likehood):
	like = []
	for i in range(2):
		like.append([])
	for word in uniqueWord:
		for i in range(2):
			like[i].append((likehood[i][word], word))
	for i in range(2):
		like[i] = sorted(like[i])[::-1][:10]
	return like


def findPrior(wordCount):
	prior = []
	total = wordCount[0] + wordCount[1]
	for i in range(2):
		possibility = float(wordCount[i])/total
		prior.append(possibility)
	return prior


def trainingBernoulli(name):
	occurrences, wordCount, uniqueWord = readData(name)
	likehood = findLikelihood(occurrences, wordCount, uniqueWord)
	prior = findPrior(wordCount)
	odds = findOdds(uniqueWord, likehood)
	like = findlike(uniqueWord, likehood)
	return likehood, prior, odds, like
