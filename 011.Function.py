# Built-in Functions
print(abs(10))       # Result : 10
print(abs(-10))      # Result : 10
print(max(1, 2, 3))  # Result : 3
print(max(2, 3))     # Result : 3

# Data Type Converting Functions
print(int(3.14159))  # Result : 3
print(float(1))      # Result : 1.0
print(str(-5.75))    # Result : -5.75
print(bool(0))       # Result : False

# Functions is a variable
print(abs)     # Result : <built-in function abs>

a = abs        # Assign a function to a variable
print(a(-10))  # Result : 10

abs = 123      # Assign a variable to a function
print(abs)     # Result : 123
