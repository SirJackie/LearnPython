#
# Slice
# Format : list[begin:end:step]
# Return : [begin, begin+1, begin+2, ..., end-3, end-2, end-1]  (not including end)
# Default Value : list[firstOne:lastOne:1]  (this is what list[:] is)
#

# Define a List with list(range()) functions
L = list(range(100))
print(L)            # Result : [0, 1, 2, ..., 97, 98, 99]


#
# Standard Selection
#

# Standard Format
print(L[10:20])     # Result : [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# Omit the begin
print(L[0:10])      # Result : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[:10])       # Result : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Omit the end
print(L[90:100])    # Result : [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(L[90:])       # Result : [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# Omit begin and end
print(L[:])         # Result : [0, 1, 2, ..., 97, 98, 99]


#
# Reverse Selection
#

# Standard Format
print(L[-20:-10])   # Result : [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]

# Omit the begin with Reverse Selection
print(L[0:-10])     # Result : [0, 1, 2, ..., 87, 88, 89]
print(L[:-10])      # Result : [0, 1, 2, ..., 87, 88, 89]

# Omit the end with Reverse Selection
print(L[-100:100])  # Result : [0, 1, 2, ..., 97, 98, 99]
print(L[-100:])     # Result : [0, 1, 2, ..., 97, 98, 99]
print(L[-100:-1])   # Result : [0, 1, 2, ..., 97, 98]
# This is because the slice not including the end
# L[-1] means 99, so 99 is not included
# And there is no L[-0], because -0 == 0
# So you can only write the end using NOT REVERSE SELECTION!!!


#
# Slice with Step
#

print(L[0:100:2])   # Result : [0, 2, 4, ..., 94, 96, 98]
print(L[::5])       # Result : [0, 5, 10, ..., 85, 90, 95]


#
# Slice with different Types of Value
#

tup = (0, 1, 2, 3, 4)
print(tup[1:-1])  # Result : (1, 2, 3) , sliced tuples are still tuples

s01 = "01234"
print(s01[1:-1])  # Result : 123 , sliced strings are still strings


