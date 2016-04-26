MAX_NUM = 2000000

def prime():
    primeList = []
    num = 2
    while 1:
        for p in primeList:
            if num % p == 0: break
            if num ** .5 < p: 
                primeList.append(num)
                yield num;break
        else:
            primeList.append(num)
            yield num
        num += 1

r = 0
for v in prime():
    if MAX_NUM < v: break
    r += v
print(r)
