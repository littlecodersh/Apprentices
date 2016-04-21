a=1
b=2
s=b
c=0
while (c<=4000000):
	c=a+b
	if c%2==0:
		s=s+c
	a=b
	b=c
print(s)