# Create str2float() function to convert string into float

from functools import reduce

def spliter(s):
    beforeDot = None
    afterDot = None
    for i in range(len(s)):
        if s[i] == ".":
            beforeDot = s[:i]
            afterDot = s[i+1:]
    return beforeDot, afterDot

def floater(beforeDot, afterDot):
    for i in range(len(str(afterDot))):
        afterDot = afterDot / 10
    return beforeDot + afterDot

def str2float(s):
    splitedProd = spliter(s)
    intProd = list(map(int, splitedProd))
    finalProd = reduce(floater, intProd)
    return finalProd

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print("Accepted")
else:
    print("Rejected")
