def bubble(n):
	for i in range(len(n)-1 , 0 , -1):
		print '\n'
		print 'Before sort:',n[:i]
		for j in range(0,i):
			if n[j] > n[j+1]:
				n[j],n[j+1] = n[j+1],n[j]
			print 'After sort:',n
	return n

t = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
print bubble(t)
