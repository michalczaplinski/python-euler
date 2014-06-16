def evenfib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        if b%2 == 0:
            result.append(b)
        a, b = b, a+b
    return result

print evenfib(4000000)
print sum(evenfib(4000000))