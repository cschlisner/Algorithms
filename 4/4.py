def qs(a, p, r):
	if (p < r):
		q = part(a, p, r)
		qs(a, p, q-1)
		qs(a, q+1, r)

def part(a, p, r):
	x = a[r]
	i = p-1
	for j in range(p, r):
		if a[j] <= x :
			i += 1
			exc(a, i, j)
	exc(a, i+1, r)
	return i+1

def exc(a, x, y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp



def threea(a, k):
	for n in range(len(a)):
		if (n+k < len(a)):
			qs(a, n, n+k)
		else: qs(a, n, len(a)-1)

def threeb(a, k):
	tmp = 0
	for n in range(len(a)):
		for j in range(1, k):
			if (n+j < len(a) and a[n] > a[n+j]):
				tmp = a[n]
				a[n] = a[n+j]
				a[n+j] = tmp

A = [1,4,2,3,15,5]
B = []
B.extend(A)

threea(A, 2)
print(A)
threeb(B, 3)
print(B)