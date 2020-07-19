# Python is a Dynamic Language, Variables' type can be changed!
a = 123
a = "abc"
a = True
a = None
print(a)

# Programming is not the same as the Mathematics
x = 10
x = x + 2
print(x)    # the result is 12

# Python does not have pointer
a = "ABC"
b = a
a = "XYZ"
print("A:", a, "B:", b)  # result: A: XYZ B: ABC

# Python's division use float by default, use // to divide with int
print(10 / 3)
print(10 // 3)
print(10 % 3)

# Python supports high precision by default!
veryLongInterger = 100000000000000000000000000000000000000000000000000000000000000000
veryLongInterger += 1
print(veryLongInterger)
