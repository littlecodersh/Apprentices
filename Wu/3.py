L = []
z = []
x = 1
i = 1
while 1:
	x=x+1
	if x > 600851475143:
           break
	if 600851475143 % x ==0:
	   L.append(x)
	   continue
for x in L:
	i=i+1
	if i>x:
		break
	if x % i !=0:
       z.append(x)
print max(z)
