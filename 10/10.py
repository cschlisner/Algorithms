
# assume g is a dict of adjacency lists of a simple undirected bipartite graph
# g[1] = the adjacency list for vertex 1 , containing names of other verticies
def MaxMatching(g):
	# we need to create a new, directed, weighted graph 'gflow' for max flow
	# gflow is a dictionary of {'node name' : [list of edges from this node]}
	# each edge will be represented as a 3-tuple: (dest vertex, capacity, flow)
	gflow = {n+1 : [] for n in range(len(g))}
	v1 = set()
	v2 = set()
	# add all of the edges from g, add verticies in edges to groups v1 and v2
	# set all residual capacities to 1
	for v in g.keys():
		if v not in v2:
			v1.add(v) 
		for e in g[v]:
			# only add edges from v1 -> v2
			if v in v1:
				gflow[v].append((e, 1, 0))
				v2.add(e)
			else: v1.add(e)

	# fully connect s -> {v1}
	gflow['s'] = [(v, 1, 0) for v in v1]
	# fully connect {v2} -> t
	gflow['t'] = []
	for u in v2:
		gflow[u].append(('t', 1, 0))
	
	# solve max flow on g with Ford-Fulkerson:
	sigma = DFS(gflow, 's', 't')
	while sigma is not None:
		minCap = 10**4
		for n in range(len(sigma)-1):
			for e in gflow[sigma[n]]:
				if e[0] == sigma[n+1] and e[1] < minCap:
						minCap = e[1]
		for n in range(len(sigma)-1):
			for i, e in enumerate(gflow[sigma[n]]):
				if e[0] == sigma[n+1]:
					gflow[sigma[n]][i] = (e[0], e[1]-minCap, e[2]+minCap)
		sigma = DFS(gflow, 's', 't')

	# add all saturated edges between v1 and v2 into a map
	match = {}
	for v in v1:
		for e in gflow[v]:
			if e[1] == 0: # no residual capacity
				match[v] = e[0]
	return v1, v2, gflow, match

# assume gf is a flow graph in the form of a dictionary {'name':[edges]} 
def DFS(gf, s, t):
	pred = {k:None for k in gf.keys()}
	old = {k:False for k in gf.keys()}
	sigma = []
	Q = [s]
	while (len(Q) > 0):
		v = Q.pop()
		if not old[v]:
			old[v] = True
			for e in gf[v]:
				if e[1] > 0: 
				# there is still residual capacity on this edge
					if e[0] == t: 
					# we found a path 
						sigma.insert(0,t)
						p = v
						while p is not None:
							sigma.insert(0,p)
							p = pred[p]
						return sigma
					pred[e[0]] = v
					Q.append(e[0])
	return None

ex = {1:[8], 2:[7,8,9], 3:[10,7,11], 4:[8,9,10], 5:[9,11], 
		6:[11], 7:[2,3], 8:[1,2,4], 9:[2,4,5], 10:[3,4], 11:[3,5,6]}

v1, v2, gf, m = MaxMatching(ex)

print("flow graph:: ")
for k in gf.keys():
	print(" %s : %s"%(k, gf[k]))
print("v1:: %s"% v1)
print("v2:: %s"% v2)
print("Matching:: %s"%m)


def MergeSort(A):
	t = 0 # not counting ops related to counting ops
	n = len(A) 
	t += 1 # len() on a list is an atomic op
	
	if n == 1:
		return A, t
	
	l = MergeSort(A[:int(n/2)])[0] 
	t += 1 + int(n/2) # assignment + list copy
	
	l.extend(MergeSort(A[int(n/2):])[0]) 
	t += n # copy + extend

	sA, s = Merge(l, int(n/2)) # s = atomic ops in Merge()
	
	return sA, (s+t) 

def Merge(A, m):
	i = 0 
	j = m # start of second sorted half
	sA = []
	t = 3 # assignments, allocation
	while len(sA) < len(A):
		if i < m and j < len(A) and A[i] < A[j]:
			sA.append(A[i])
			i += 1
		elif j < len(A):
			sA.append(A[j])
			j += 1
		elif i < m:
			sA.append(A[i])
			i += 1
		t += 10 # conditions + append + re-assign
	return sA, t

import random as r
def randomArray(n):
	return [r.randint(1,n) for i in range(n)]

# avgs = []
# for n in range(4,25):
# 	print(n,end=': ')
# 	s = 0
# 	for i in range(5):
# 		s += MergeSort(randomArray(2**n))[1]
# 	s /= 5
# 	avgs += (n, s)
# 	print(s)

# print(avgs)

