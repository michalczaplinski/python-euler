def isPrime(n):
    for i in xrange(2, ((n+1)/2)+1):
        if n%i == 0:
            return False
    else:
        return True

def listPrimes(m):
    #primes = [ x for x in range(m + 1) if isPrime(x) ]
    primes = []
    x = 2
    while True:
        if isPrime(x):
            primes.append(x)
        if len(primes) == m:
            return primes
        x = x+1

print listPrimes(10001)[-1]


