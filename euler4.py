def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

pali = 0

for n in range(111, 1000):
    for m in range(111, 1000):
        if isPalindrome(n*m):
            if n*m > pali:
                pali = n*m

print pali