import numpy as np
import random 


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def alignStrings(x,y):
	costS = 12
	costT = 13
	costID = 1

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
				cost.append(S[i-2][j-2] + costT
							+ (0 if (x[i-1] == y[j-2]) else 1)
							+ (0 if (y[j-1] == x[i-2]) else 1))
			
			# Sub -- i-1,j-1
			cost.append(S[i-1][j-1] + (costS if x[i-1] != y[j-1] else 0))
			
			# insert -- i,j-1
			cost.append(S[i][j-1] + costID)
			
			# delete -- i-1,j
			cost.append(S[i-1][j] + costID)

			S[i][j] = min(cost)
	return S

def extractAlignment(S,x,y):
	costS = 12
	costT = 13
	costID = 1
	optimaledits = []
	optimalpath = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
	i = len(x)
	j = len(y)
	while i > 0 or j > 0:
		optimalpath[i][j] = 1
		# build cost array of tuples = (symbol, cost)		
		cost = []
		cost.append(("s", S[i-1][j-1] + (costS if x[i-1] != y[j-1] else 0))) 
		cost.append(("i", S[i][j-1] + costID))
		cost.append(("d", S[i-1][j] + costID))
		if j > 1 and i > 1:
			cost.append(("t", S[i-2][j-2] + costT 
							+ (0 if (x[i-1] == y[j-2]) else 1)
							+ (0 if (y[j-1] == x[i-2]) else 1)))
		# the current optimal value is the minimum of cost
		optval = S[i][j]
		
		# choose one of the edits at random that have the same cost 
		# as the current optimal value 
		opt = random.choice([c[0] for c in cost if c[1] == optval])
		
		# if the characters in both strings were the same (and it was a sub),
		# then insert "|" (no-op) at the beginning of the list
		if (opt == "s" and x[i-1] == y[j-1]):
			optimaledits.insert(0, "|")

		# otherwise insert the operation 
		else: optimaledits.insert(0,opt)

		# update the indicies to the selected subproblem
		if opt == "s":
			i -= 1
			j -= 1
		elif opt == "i":
			j -= 1
		elif opt == "d":
			i -= 1
		elif opt == "t":
			optimaledits.insert(0,opt)
			i -= 2
			j -= 2
	return optimaledits, optimalpath

def commonSubstrings(x,L,a):
	substr = [""]
	k = 0
	for i in range(len(a)):
		if a[i] == "|":
			substr[-1] += x[i-k]
		else: 
			if a[i] == "i":
				k += 1
			substr.append("")
	return [s for s in substr if len(s) >= L]

def readFile(file):
	string = ""
	with open(file, 'r') as f: # read names from lastnames.txt
		for ln in f:
			string+=ln.strip()
	return string

# X = readFile("data/x.txt")
# Y = readFile("data/y.txt")
X = "EXPONENTIAL"
Y = "POLYNOMIAL"
print(X)
print()
print(Y)

t = alignStrings(X,Y)

print("_____ S ______")
print(np.matrix(t))

edits, path = extractAlignment(t,X,Y)
print("\n_______ Path ______")
print(np.matrix(path))
print()

k = 0
for ch in range(len(edits)):
	if edits[ch] == "i":
		print("-",end='')
		continue
	elif edits[ch] == "s":
		print(colors.FAIL,end='')
	elif edits[ch] == "d":
		print(colors.FAIL,end='')
	elif edits[ch] == "|":
		print(colors.OKGREEN,end='')
	elif edits[ch] == "t":
		print(colors.OKBLUE,end='')
	print((X[k] if (X[k] != " ") else "_"),end='')
	print(colors.ENDC,end='')
	k += 1
print()

print("\n______ Common Substrings_____")
for cs in commonSubstrings(X, 9, edits):
	print("\\item \"%s\""%cs)
