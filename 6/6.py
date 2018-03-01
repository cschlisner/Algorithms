W = [(3, 51), (6, 60), (6, 99), (105, 155), (121, 178), (86, 186)]

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

print(greedyAdTimes(W))

