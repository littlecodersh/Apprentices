def prime():
    primeList = []
    num = 2
    while 1:
        for p in primeList:
            if num % p == 0: break
        else:
            primeList.append(num)
            yield num
        num += 1

for i, v in enumerate(prime()):
    if 10001 == i + 1: print(v);break
