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
		j = 0
		t = {i+1:1}
		while j < len(g[i]):
			if g[i][j] in t:
				g[i].pop(j)
			else: 
				t[g[i][j]] = 1
				j += 1

def convert(g):
	gprime = [[]]
	for i in range(len(g)):
		r = [False for k in range(len(g))]
		for e in g[i]:
			if e != i+1:
				r[e-1] = True
		gprime[i] = [e+1 for e in range(len(g)) if r[e]]
	g = gprime
					
G = gen_data(5)

printmeme(G)

fixmeme(G)
print("____ FIXED MEMES _____")
printmeme(G)
