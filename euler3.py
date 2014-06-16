wdef isPrime(n):
    for i in xrange(2, ((n+1)/2)+1):
        if n%i == 0:
            return False
    else:
        return True

def findFactors(n, factors):
    for f in xrange(2, n+1):
        if isPrime(f) and n % f == 0:
            factors.append(f)
            return findFactors((n/f), factors)
    return factors

factors = []
factors = findFactors(600851475143, factors)
print max(factors)
