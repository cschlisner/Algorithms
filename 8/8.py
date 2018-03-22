import random as r
import numpy as np

def gen_data(n):
	return [[r.randint(1,n) for i in range(r.randint(1,n))] for x in range(n)]


def printmeme(g):
	i = 1
	for row in g:
		print(i, row)
		i += 1

def fixmeme(g):
	for i in range(len(g)):
		adj = [] 
		j = 0
		while j < len(g[i]):
			if g[i][j] == i+1:
				g[i].pop(j)
			elif g[i][j] in adj:
				g[i].pop(j)
			else: 
				adj.append(g[i][j])
				j += 1
G = gen_data(5)

printmeme(G)

fixmeme(G)
print("____ FIXED MEMES _____")
printmeme(G)
