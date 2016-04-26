s = set([])
x = 0
while 1:
	x = x + 1
	if x >1000:
		break
	if x % 3 == 0:
		continue
		s.add(x)
	if x % 5 == 0:
		s.add(x)
		continue
print sum(s) 

        
