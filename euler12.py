#def findFactors(n, factors):
#    for f in xrange(2, n+1):
#        if isPrime(f) and n % f == 0:
#            factors.append(f)
#            return findFactors((n/f), factors)
#    return factors


def isPrime(n):
    for i in xrange(2, ((n+1)/2)+1):
        if n%i == 0:
            return False
    else:
        return True

def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n:
            break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1:
        factors.append((n, 1))
    return factors

def findDivisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in xrange(r + 1)]
    return div

n = 1
primes = [ x for x in xrange(1, 10000000) if isPrime(x) ]
while True:
    total = sum(xrange(n))
    factors = factorize(total, primes)
    divisors = findDivisors(factors)
    n+=1
    total = total + n
    if len() > 500:
        break

print total
