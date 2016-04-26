def prime(num):
	for fac in range(2,int(num**0.5)+1):
		if num%fac==0:
			return False
	return True


sum_=2
for i in range(3,2000000):
	test_result=prime(i)
	if test_result:
		sum_+=i
print sum_
		






