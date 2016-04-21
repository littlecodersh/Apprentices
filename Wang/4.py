f=0
a=997
while a >=100 and f==0:
	x=int(a/100)
	y=int((a-x*100)/10)
	z=a-100*x-10*y
	b=x+10*y+100*z+1000*a
	for i in range (999,100,-1):
		if b%i==0:
			if (b/i)<=999 and (b/i)>=100:
				f=1
				break
	a=a-1
print (b)
		


