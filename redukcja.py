res = []
# def checkCondition(tuple):


def saveResultToFile(arrays):
	outputFile = open("arrays.txt", "w+")
	for array in arrays:
		data = str(array) + '\n'
		outputFile.write(data)
	outputFile.close()
	
	
def req(tuple, dictionary):
	#print("------dictionary[",len(dictionary),"]: ",dictionary)
	#print("tuple: ",tuple)
	root = tuple[:]
	for key in dictionary:
		r = root[:]
		#print("key: ",key)
		r.append(key)
		#print("r(after): ",r)
		#print("root(after): ",root)
		
		if len(dictionary[key]) == 0:
			res.append(r)
			#print("------break")
			
			break
		else:
			#print("------REQ")
			req(r, dictionary[key])

def mapDictionaryToTuples(dictionary, debug=False):
	tuple = []
	req(tuple, dictionary)
	if debug:
		saveResultToFile(res)
	return res
	
		

def reduction(dictionary, pointA, pointB):
	for key in dictionary:
		if key == pointB:
			dictionary[pointA] 
			dictionary[key]
	

# input = znajdowanie.pobierzDane()

# for tuple in input:
	# checkCondition(tuple)