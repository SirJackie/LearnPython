#
# Sorted() Function
# Format : sorted([list], key=function, reverse=True/False)
# sorted() will sort using the result processed by key() function
#

result1 = sorted([4, 9, 2, 5, 1])
print(result1)  # Result : [1, 2, 4, 5, 9]

result2 = sorted([4, 9, 2, 5, 1], reverse=True)
print(result2)  # Result : [9, 5, 4, 2, 1]

result3 = sorted([36, 5, -12, 9, -21], key=abs)
print(result3)  # Result : [5, 9, -12, -21, 36]

result4 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(result4)  # Result : ['Credit', 'Zoo', 'about', 'bob']

result5 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(result5)  # Result : ['about', 'bob', 'Credit', 'Zoo']
