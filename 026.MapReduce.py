#
# Map() Function
# Format : map(f(x), [x1, x2, x3, x4]) = [f(x1), f(x2), f(x3), f(x4)]
# Return : a Iterator, need to use list() to convert into list
#

def func(x):
    return x * x

# Square all the numbers
result1 = map(func, [1, 2, 3, 4, 5])
print(list(result1))  # Result : [1, 4, 9, 16, 25]

# Numbers 2 Strings
result2 = map(str, [1, 2, 3, 4, 5])
print(list(result2))  # Result : ['1', '2', '3', '4', '5']


#
# Reduce() Function
# Format : reduce(f(x1, x2), [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# Return : A Variable
#

from functools import reduce

def add(x, y):
    return x + y

# Sum
result3 = reduce(add, [1, 3, 5, 7, 9])
print(result3)  # Result : 25

def merge(x, y):
    return x * 10 + y

# Merge numbers together
result4 = reduce(merge, [1, 3, 5, 7, 9])
print(result4)  # Result : 13579

def char2int(ch):
    digits = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
              "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    return digits[ch]

# String 2 Int!!!
result5 = reduce(merge, map(char2int, "13579"))
print(result5)  # Result : 13579

# Package String2Int into a Function
def String2Int(s):
    digitList = map(char2int, s)          # "13579" to [1, 3, 5, 7, 9]
    mergedNum = reduce(merge, digitList)  # [1, 3, 5, 7, 9] to 13579
    return mergedNum

print(String2Int("13579"))  # Result : 13579
