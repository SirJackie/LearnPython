#
# A Simple Closure
#

def LazySum(*args):
    def Sum():
        sum = 0
        for i in args:
            sum = sum + i
        return sum
    return Sum

f = LazySum(1, 3, 5, 7, 9)
print(f)    # Result : <function LazySum.<locals>.Sum at 0x000001898CF71AF8>
print(f())  # Result : 25


#
# A Common Error About Closure
#

def Count():
    funcList = []
    for i in range(1, 4):
        def func():
            return i * i
        funcList.append(func)
    return funcList

f1, f2, f3 = Count()
print(f1())  # Expected : 1 , Result : 9
print(f2())  # Expected : 4 , Result : 9
print(f3())  # Expected : 9 , Result : 9

# This is because there is only one "i", it's inside "Count()"
# If you expected 1, 4, 9, you need to create multiple "i"

def Count():
    funcList = []
    def IEnvironment(i):
        def CalcTheLazyResult():
            return i * i
        return CalcTheLazyResult
    for x in range(1, 4):
        funcList.append(IEnvironment(x))
    return funcList

f1, f2, f3 = Count()
print(f1())  # Expected : 1 , Result : 1
print(f2())  # Expected : 4 , Result : 4
print(f3())  # Expected : 9 , Result : 9

# So don't use variables in For Statement when you make a Closure
