def get_multiples_sum(base, maxNum):
    num = base
    sumNum = 0
    while(num < maxNum):
        sumNum += num
        num += base
    return sumNum

print(get_multiples_sum(3, 1000)+get_multiples_sum(5,1000))
