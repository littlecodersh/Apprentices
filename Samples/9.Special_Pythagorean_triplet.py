def get_py_triplet(maxNum):
    for a in range(1, maxNum):
        for b in range(a + 1, (maxNum - a) / 2):
            if a * a + b * b == (maxNum - a - b) ** 2:
                return a * b * (maxNum - a - b)
print(get_py_triplet(1000))
