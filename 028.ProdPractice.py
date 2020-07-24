# Create prod() function to calculate the product of all numbers inside list

from functools import reduce

def multiply(x, y):
    return x * y

def prod(L):
    return reduce(multiply, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('Accepted')
else:
    print('Rejected')