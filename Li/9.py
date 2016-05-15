for a in range (1,334):
	for b in range (1,501):
		c=1000-a-b
		if c**2==a**2+b**2:
			s=a*b*c
			print s
			