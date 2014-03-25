def insertion_sort(n):
	if len(n) == 1:
		return n
	b = insertion_sort(n[1:])
	print 'Input arrary:' , b
	m = len(b)
	for i in range(m):
		if n[0] <= b[i]:
			print 'The loop i:',i
			print 'The loop return Array:',b[:i]+[n[0]]+b[i:]
			print '\n'
			return b[:i]+[n[0]]+b[i:]
			

	print 'Result:',b + [n[0]],'\n'
	return b + [n[0]]


tlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]

print insertion_sort(tlist)
