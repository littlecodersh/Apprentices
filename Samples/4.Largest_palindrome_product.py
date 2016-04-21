def test_palindrome(num):
    numStr = str(num)
    for i in range(len(numStr) / 2):
        if numStr[i] != numStr[-1 - i]: return False
    return True

maxPalindrome = -1

for i in xrange(1000, 100, -1):
    for j in xrange(1000, 100, -1):
        if maxPalindrome < i * j and test_palindrome(i * j):
            maxPalindrome = i * j
print maxPalindrome
