import itertools

def gcd(m, n):
    while n != 0:
        t = n
        n = m%n
        m = t
    return m

numbers = []
for m in range(2, 100):
    for n in range(1, m):
        #if (m-n) % 2 == 1 and gcd(m, n) == 1: # <-- limits the search space
            numbers.append((m, n))

def findTriple(numbers):
    for i in numbers:
        m, n = i[0], i[1]
        for k in range(1, 500):
            sum = k*((m**2)-(n**2)) + k*(2*m*n) + k*((m**2)+(n**2))
            if sum == 1000:
                print k, m, n
                return k*((m**2)-(n**2)),  k*(2*m*n),  k*((m**2)+(n**2))
            elif sum > 1000:
                break

triple = findTriple(numbers)
print triple
print sum(triple)
print triple[0] * triple[1] * triple[2]
