# Define a Function
def MyAbs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(MyAbs(10))     # Result : 10
print(MyAbs(-10))    # Result : 10
# print(MyAbs('a'))  # TypeError: bad operand type


# Define a Empty Function
def nop():
    pass

print(nop())         # Result : None


# Return Many Values (actually a tuple:)
def returner():
    return "A", "B", "C"

a = returner()
print(a[0])  # Result : A
print(a[1])  # Result : B
print(a)     # Result : ('A', 'B', 'C')
