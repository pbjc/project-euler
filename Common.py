# Common or useful functions

def isPrime(num):
    num = abs(num)
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** .5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primeSieve(bound):
    sieve = [True] * bound
    sieve[0] = sieve[1] = False
    for (i, prime) in enumerate(sieve):
        if prime:
            yield i
            for n in range(i * i, bound, i):
                sieve[n] = False

def gcd(x, y):
    if ((x % y) == 0):
        return y;
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x // gcd(x, y)) * y

def prod(factors):
    p = 1
    for n in factors:
        p *= n
    return p

def divisors(n):
    fact = set()
    for i in range(1, int(n ** .5 + 1), 1):
        if n % i == 0:
            fact.add(i)
            fact.add(n // i)
    return fact

def trianglenum(n):
    return int(0.5 * n * (n + 1))

def pentagonnum(n):
    return int(0.5 * n * (3 * n - 1))

def hexagonnum(n):
    return n * (2 * n - 1)

def isPandigital(n):
    s = str(n)
    length = len(s)
    for i in range(length):
        if s.find(str(length - i)) == -1:
            return False
        s = s.replace(str(length - i), '', 1)
    return len(s) == 0