def merge(l1,l2):
	final = []
	l1 = sorted(l1)
	l2 = sorted(l2)
	while l1 and l2:
		if l1[0] >= l2[0]:
			final.append(l2.pop(0))
		else:
			final.append(l1.pop(0))
	return final + l1 + l2

def iter_mergesort(List):
	Q = []
	for i in List:
		Q.append([i])
	while len(Q) > 1 :
		print 'Q:',Q
		Q.append(merge(Q.pop(0),Q.pop(0)))
	return Q.pop()

t1 = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]


print iter_mergesort(t1)
