r = 2
num = 600851475143
while num != 1:
    if num % r == 0:
        num /= r
    else:
        r += 1

print r
