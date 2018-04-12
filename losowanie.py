#!/etc/bin/python

# losujemy 1 000 -> 1 000 000 punktow
# zakladamy ze istnieje ok. 20 takich ze d(p1, p2) < R
# pairsiem lista par punktow spelniajacych powyzszy warunek
import math
import random
from timeit import default_timer as timer

def distance(punktA, punktB):
	return math.sqrt((punktA[0]-punktB[0])**2+(punktA[1]-punktB[1])**2)
	
def saveResultToFile(pairs):
	outputFile = open("pairs.txt", "w+")
	for pair in pairs:
		data = str(pair[0]) + ':' + str(pair[1]) + '\n'
		outputFile.write(data)
	outputFile.close()


def losujPunkty(X=100, N=100, R=10, debbug=False):

	if debbug:
		print('size: ', X)
		start = timer()

	pairs = []
	squares = {}

	for i in range (0, N):
		x = random.randint(0,X)
		y = random.randint(0,X)
		punkt = (x,y)
		
		xK = math.floor(x/R)
		yK = math.floor(y/R)
		square = (xK, yK)

		if not square in squares:
			squares[square] = []

		k = []
		for j in [-1, 0, 1]:
			for l in [-1, 0, 1]:
				key = (xK+j, yK+l)
				if key in squares:
					k.extend(squares[key])
		
		squares[square].append(punkt)
		
		for punktB in k:
			if distance(punkt, punktB) < R:
				pairs.append((punkt, punktB))

	if debbug: 
		saveResultToFile(pairs)
		end = timer()
		print('Time: ', end - start)
	
	return pairs