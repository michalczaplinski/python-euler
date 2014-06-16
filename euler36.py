total = 0
for i in xrange(1000000):
    s10 = str(i)                # string decimal base
    if s10 == s10[::-1]:
        s2 = str(bin(i)[2:])    # string binary
        if s2 == s2[::-1]:
            total += i
print total
