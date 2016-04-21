num=600851475143
def a(x):
	i=2
	while i!=x:
		if x%i==0:
			x=x/i
		else:
			i+=1
	return i

r=a(num)
print(r)
