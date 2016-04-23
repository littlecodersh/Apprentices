_sum_of_squares=0
_square_of_sum=0
for i in range (1,101):
	_sum_of_squares+=(i*i)
	_square_of_sum+=i

_square_of_sum*=_square_of_sum
dif=_square_of_sum - _sum_of_squares
print(dif)
