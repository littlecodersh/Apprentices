def factor_storage():
    def get_factor_count(baseNum, factor):
        i = 0
        while baseNum % factor == 0:
            baseNum /= factor
            i += 1
        return i
    def get_factor_list(baseNum):
        i = 2
        l = []
        while baseNum != 1:
            if baseNum % i == 0:
                baseNum /= i
                if not i in l: l.append(i)
            else:
                i += 1
        return l
    factorDict = {}
    while 1:
        baseNum = yield
        if baseNum == -1:
            break
        elif 1 < baseNum:
            for factor in get_factor_list(baseNum):
                fc = get_factor_count(baseNum, factor)
                if factorDict.get(factor, -1) < fc: factorDict[factor] = fc
    yield factorDict

fs = factor_storage()
fs.next()

for baseNum in range(1, 21): fs.send(baseNum)

r = 1
for factor, count in fs.send(-1).items():
    r *= factor**count
print(r)
