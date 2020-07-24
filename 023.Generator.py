#
# Create a Generator (List Comprehension Way)
#

# Create a List Comprehension
L = [x * x for x in range(1, 11)]
print(L)  # Result : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a Generator
g = (x * x for x in range(1, 11))
print(g)  # Result : <generator object <genexpr> at 0x000001ED1168C5C8>


#
# Iterate a Generator
#

# Way1
# print(next(g))  # not recommended

# Way2
for n in g:
    print(n)  # Result : 1 4 9 16 25 36 49 64 81 100

#
# Create a Generator (Function Way)
#

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)  # Result : <generator object fib at 0x000001F2470AA7C8>

for i in f:
    print(i)  # Result : 1 1 2 3 5 8 , you can't get "done" from return statement


#
# Get Return Value From a Generator
#

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# Result :  # g: 1  # ...  # g: 8  # Generator return value: done
