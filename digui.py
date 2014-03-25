def digui(n):
	if len(n) == 1:
		return n
	a = digui(n[1:])
	print a
	b = a + [n[0]]	
	print b,'\n'
	return b

tlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]

print digui(tlist)
