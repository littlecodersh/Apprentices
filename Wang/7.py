def prime():
	num=2
	while 1:
		num+=1
		flag=0
		for fac in range(2,int(num**0.5)+1):
			if num%fac==0:
				flag=1
				break
		if flag==0:yield num


k=1	
for i in prime():
	k+=1
	if k>=10001:break
print i
		






