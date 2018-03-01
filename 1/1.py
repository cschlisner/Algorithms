
A = range(10)
V = 4


def findV(a, v):
	for i in range(1, len(a)-1):
		if a[i] == v:
			return i;
	return null

def findCommon(A, B):
	ai = bi = 0
	while (bi < len(B) and ai < len(A)):
		if (A[ai]==B[bi]):
			return True
		if (A[ai] < B[bi]):
			ai += 1
		elif (B[bi] < A[ai]):
			bi += 1
	return False

print(findCommon([1,2,3,41], [7,16,17,41,42]))