import losowanie

dictionary = {}

def saveResultToFile(dictionary):
	outputFile = open("dictionary.txt", "w+")
	for key in dictionary:
		data = str(key) + ':' + str(dictionary[key]) + '\n'
		outputFile.write(data)
	outputFile.close()

def makeForest(dict):
	for key in dict:
		if key in dictionary:
			for k in dictionary[key]:
				if k in dict:
					dict[key][k] = dict[k]

def mapPairsToDictionary(pairs):
	for pair in pairs:
		pointA = pair[0]
		pointB = pair[1]
		
		if not pointA in dictionary:
			dictionary[pointA] = {}
			
		dictionary[pointA][pointB] = {}

def znajdzKrawedzie(pairs, debug=False):
	mapPairsToDictionary(pairs)
		
	for key in dictionary:
		makeForest(dictionary[key])
	
	if debug:
		saveResultToFile(dictionary)
	return dictionary