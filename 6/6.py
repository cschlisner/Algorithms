import random as rnd


def generateTestRangeData(n, maximum):
    s = [rnd.randint(0, maximum) for i in range(n)]
    e = [x+rnd.randint(0, maximum-x) for x in s]
    return [(s[i], e[i]) for i in range(n)]

def greedyAdTimes(w):
    remaining = list(w)
    ads = []
    i = 1
    while len(remaining) > 0:
        print("remaining wizards: ", remaining)
        ej = (min(remaining, key=lambda x:x[1]))[1]
        print("ad",i,": ", ej)
        i += 1
        ads.append(ej)
        remaining = list(filter(lambda x: x[0] > ej or ej > x[1], remaining))
    return ads

# W = [(3, 51), (6, 60), (6, 99), (105, 155), (121, 178), (86, 186)]
# print(greedyAdTimes(W))

def greedyRanges(r):
    S = list(r)
    u = 0 # latest uncovered time
    T = [] # list of selected ranges
    maxl = max([x[1] for x in S])
    while u < maxl:  
        print("u: ", u)
        maxrg=(0,0)
        for rg in S:
            print("rg: ", rg)
            if (rg[0] <= u and rg[1] > u and rg[1] - u > maxrg[1] - u):
                maxrg = rg
        if maxrg == (0,0):
            u = min([x[1] for x in S])
            continue
        u = maxrg[1]
        T.append(maxrg)
        S.remove(maxrg)
    return T

data = generateTestRangeData(4, 24)
print(data)

print(greedyRanges(data))


