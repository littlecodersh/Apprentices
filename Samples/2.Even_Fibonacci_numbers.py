def get_fib():
    i = 0
    j = 1
    while 1:
        i += j
        yield i
        j += i
        yield j

r = 0
for i in get_fib():
    if 4e6 <= i: break
    if i % 2 == 0: r += i
print(r)
