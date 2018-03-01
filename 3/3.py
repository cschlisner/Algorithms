def qs(a, p, r):
	if (p < r):
		q = part(a, p, r)
		qs(a, p, q-1)
		qs(a, q+1, r)

def part(a, p, r):
	x = a[r]
	i = p-1
	for j in range(p, r):
		print(a[p:r+1], "a[j]=", a[j], "x=",x, ("*" if (x==3 or a[j]==3) else ""))
		if a[j] <= x :
			i += 1
			exc(a, i, j)
	exc(a, i+1, r)
	return i+1

def exc(a, x, y):
	tmp = a[x]
	a[x] = a[y]
	a[y] = tmp

A = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
qs(A, 0, len(A)-1)
print(A)

def sumarr(A):
	n = len(A)
	m = [[0 for x in range(n)] for y in range(n)]
	for i in range(0, len(A)-1):
		m[i][i+1] = A[i]+A[i+1]
		for j in range(i+2, len(A)):
			m[i][j] = m[i][j-1]+A[j]
	return m

print(sumarr([1,2,3,4]))