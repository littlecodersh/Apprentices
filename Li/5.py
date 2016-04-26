p=1
for i in range(2,21):
	k=2
	b=p
	a=i
	while a!=1:
		if a%k==0:
			if b%k==0:
				b/=k
			else:
				p=p*k
			a/=k
		else:
			k+=1
print p
