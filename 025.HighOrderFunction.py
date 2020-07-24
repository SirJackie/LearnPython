#
# Functions are Variables
#

# Variable = Function
print(abs)  # Result : <built-in function abs>
f = abs
print(f)    # Result : <built-in function abs>

# Function = Variable
abs = 10
print(abs)  # Result : 10
abs = f

#
# Functions can be Arguments, because Variables can be Arguments
# This is what High-order Function means
#

def Add(x, y, func):
    return func(x) + func(y)

print(Add(-5, 6, abs))  # Result : 11
