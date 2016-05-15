p=2
k=2
s=0
while p<2000000:
	if p%k==0:
		if p<=k:
			s+=p
		p+=1
		k=2
	else:
		k=k+1
print s