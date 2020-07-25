def OddIterator():
    n = 1
    while True:
        n = n + 2
        yield n

def NotDivisible(n):
    return lambda x: x % n > 0

def CreatePrimeGenerator():
    yield 2
    it = OddIterator()
    while True:
        n = next(it)
        yield n
        it = filter(NotDivisible(n), it)

g = CreatePrimeGenerator()

for prime in g:
    if prime > 100000:
        break
    print(prime)
