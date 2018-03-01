#A = [7,6,4,-1,-2,-9,-5,-3,10,13]


A = [7,6,4,-1,-2,-9,-3,-5,10,13,14,-3,-71,-5,-3]

def globalmin(a, i):
	return globalmin(a, i+1) if (a[i] > a[i+1]) else a[i]

def mm(a, i):
	while (a[i] > a[i+1]):
		i += 1
	if (i < (len(a)-(len(a)/3))):
		return min(a[i], mm(a, (len(a)-(len(a)/3))))
	return a[i]

print(mm(A, 0));