#
# Define a Lambda Function
#

f = lambda x: x * x

print(f(5))  # Result : 25
print(f(6))  # Result : 36
print(f(7))  # Result : 49


#
# Give Lambda Function as Argument
#

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))  # Result : [1, 4, 9, 16, 25]


#
# Give Lambda Function as Return Value
#

def CreateLazyEvaluation(x, y):
    return lambda: x * y

LazyEvalObject = CreateLazyEvaluation(11111, 11111)

print(LazyEvalObject)    # Result : <function ...<lambda> at ...>
print(LazyEvalObject())  # Result : 123454321

