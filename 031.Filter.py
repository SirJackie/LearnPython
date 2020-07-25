#
# Filter() Function
# Format : filter(f(x), [x1, x2, x3, x4])
# If f(x1) == True, x1 will be retained, The rest will be thrown away
# Return : a Iterator, need to use list() to convert into list
#

def func(x):
    if x % 2 == 0:
        return True
    return False

result1 = filter(func, [1, 2, 3, 4, 5, 6])
print(list(result1))  # Result : [2, 4, 6]
