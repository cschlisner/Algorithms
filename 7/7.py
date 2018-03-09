import numpy as np
import random 

def alignStrings(x,y):
	# Y on top, X on side as in example
	S = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
	
	# base cases = cost of aligning empty strings 
	for j in range(len(y)+1):
		S[0][j] = j
	for i in range(len(x)+1):
		S[i][0] = i

	for i in range(1,len(x)+1):
		for j in range(1,len(y)+1):
			cost = []
			# Swap -- i-2,j-2
			if j > 1 and i > 1:
				cost.append(S[i-2][j-2] + 3)
			# Sub -- i-1,j-1
			cost.append(S[i-1][j-1] + (1 if x[i-1] != y[j-1] else 0))
			# insert -- i,j-1
			cost.append(S[i][j-1] + 1)
			# delete -- i-1,j
			cost.append(S[i-1][j] + 1)

			S[i][j] = min(cost)
	return S


def extractAlignment(S,x,y):
	ops = ["sub","ins","del","swap"]
	optimaledits = []
	optimalpath = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
	i = len(x)
	j = len(y)
	while i > 0 or j > 0:
		optimalpath[i][j] = 1
		cost = [S[i-1][j-1], S[i][j-1], S[i-1][j]]
		if j > 1 and i > 1:
			cost.append(S[i-2][j-2])
		
		optval = min(cost)
		# list of indicies of instances of optimal value
		optindices = [k for k, c in enumerate(cost) if c == optval]
		# choose one at random
		opt = ops[random.choice(optindices)]
		
		# insert the operation at the beginning of the list
		# if there was no change in cost from the previous optimal value, 
		# then insert "nop" (no-op)
		optimaledits.insert(0, "nop" if (S[i][j] == optval) else opt)

		if opt == "sub":
			i -= 1
			j -= 1
		elif opt == "ins":
			j -= 1
		elif opt == "del":
			i -= 1
		elif opt == "swap":
			i -= 2
			j -= 2

	return optimaledits, optimalpath

X = "exponential"
Y = "polynomial"
t = alignStrings(X,Y)
print(np.matrix(t))
edits, path = extractAlignment(t,X,Y)
print(edits)
print(np.matrix(path))