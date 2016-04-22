key=1
for i in range (2,21):
	if key%i != 0:
		a=i
		b=key
		k=2
		while a!=1:
			if a%k==0:
				a/=k
				if b%k!=0:
					key*=k
				else:
					b/=k
			else:
				k+=1				
print(key)

