max=0
for m in range (100,999):
	for n in range (100,999):
		p=m*n
		f=(int(p/100000));
		e=(int(p/10000)-10*int(p/100000))
		d=(int(p/1000)-10*int(p/10000))
		c=(int(p/100)-10*int(p/1000))
		b=(int(p/10)-10*int(p/100))
		a=(p-10*int(p/10))
		if (a==f and b==e and c==d):
			s=p
			if max<s:
				max=s
print max

