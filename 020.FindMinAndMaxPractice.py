def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# Test
if findMinAndMax([]) != (None, None):
    print('Rejected')
elif findMinAndMax([7]) != (7, 7):
    print('Rejected')
elif findMinAndMax([7, 1]) != (1, 7):
    print('Rejected')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('Rejected')
else:
    print('Accepted')
