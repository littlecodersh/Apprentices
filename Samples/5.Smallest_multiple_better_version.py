multiple = 1
for baseNum in range (1,21):
    if multiple % baseNum == 0: continue
    tmpMul = multiple
    factor = 2
    while baseNum != 1:
        if baseNum % factor == 0:
            baseNum /= factor
            if tmpMul % factor == 0:
                tmpMul /= factor
            else:
                multiple *= factor
        else:
            factor += 1
print(multiple)
