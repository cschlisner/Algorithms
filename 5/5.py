import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import string
import math
import random
 
# original list was downloaded as 'data.txt'
# 'lastnames.txt' was generated with the unix command: cut -d ' ' -f 1 data.txt > lastnames.txt

# l = 200 # number of buckets
# x = []  # list of locations hashed to

# xx = [0 for i in range(200)] # number of collisions at each location

# longestChain = [0 for i in range(1000)]

# hashing function h(x)
def h(s):
	charsum = 0
	for c in s:
		charsum += string.ascii_uppercase.index(c) + 1
	return charsum % l

# pick n/2 unique random indexes from [0..n]
# print("picking random names....")
# totalNames = 88800 
# chosenOnes = []
# while (len(chosenOnes) < 1000):
# 	randInd = np.random.random_integers(totalNames)
# 	if randInd not in chosenOnes:
# 		chosenOnes.append(randInd)

# print("hashing....")
# with open("lastnames.txt", 'r') as f: # read names from lastnames.txt
# 	i=0
# 	for lname in f:
# 		i += 1
# 		# if (i in chosenOnes): # filter randomly choosen names by index
# 		loc = h(lname.strip())
# 		xx[loc] += 1 # add this hash location to the list
# 		if xx[loc] > longestChain[i-1]:
# 			longestChain[i] = xx[loc]
# 		else: 
# 			longestChain[i] = longestChain[i-1]
# 		if i == len(longestChain)-1:
# 			break

# unfilledBuckets = 200
# i=0
# while unfilledBuckets > 0:
# 	lname = ''.join(random.choice(string.ascii_uppercase) for n in range(10))
# 	i += 1
# 	# if (i in chosenOnes): # filter randomly choosen names by index
# 	loc = h(lname.strip())
# 	if xx[loc] == 0:
# 		unfilledBuckets -= 1 # we have filled a new bucket
# 	xx[loc] += 1 # add this hash location to the list
# 	if unfilledBuckets == 0:
# 		print("FILLED BUCKETS AT N=", i)
# 		break
# print("items=", i)
# for n in range(200):
# 	print(n, xx[n])

# plt.plot(longestChain)
# plt.plot(np.unique(range(len(longestChain))), np.poly1d(np.polyfit(range(len(longestChain)), longestChain, 1))(np.unique(range(len(longestChain)))), "--")
# plt.plot([math.log(n) for n in range(1, len(longestChain))])
# plt.title(r'Longest Chain using h(x) vs Number of items hashed')
# plt.ylabel('Longest Chain')
# plt.xlabel('Number of items')
# plt.show()

# produce a histogram
# n, bins, patches = plt.hist(x, l, normed=0, facecolor='blue', alpha=0.5)
# plt.xlabel('Hash Location')
# plt.ylabel('Collisions')
# plt.title(r'Distribution of Hash Locations')
# plt.subplots_adjust(left=0.15)
# plt.show()





################## 3

def wizardChange(n,v):
	r = len(v)
	d = [0 for i in range(r)]
	while n > 0: 
		k = r-1
		while ( k >= 0 and v[k] > n):	
			k -= 1
		n = n - v[k]
		d[k] += 1
	return d, sum(d)

coins = [1,5,10,25]

for x in range(500):
	d, s = wizardChange(x,coins)
	print(x, d, s)





