#
# Iterate a List
#

L = ["a", "b", "c", "d", "e"]

for i in L:
    print(i)  # Result : a b c d e


#
# Iterate a Dict
#

D = {"a": 1, "b": 2, "c": 3}

for key in D:
    print(key)  # Result : a b c

for value in D.values():
    print(value)  # Result : 1 2 3

for key, value in D.items():
    print(key, value)  # a 1 b 2 c 3


#
# Iterate a String
#

S = "Alphabet"

for char in S:
    print(char)  # Result : A l p h a b e t


#
# Judge if a variable is Iterable
#

from collections import Iterable

print(isinstance(L, Iterable))    # List is Iterable
print(isinstance(D, Iterable))    # Dict is Iterable
print(isinstance(S, Iterable))    # String is Iterable
print(isinstance(123, Iterable))  # Result : False , Int is not Iterable


#
# Use Index to Iterate a List
#

for i, value in enumerate(L):
    print(i, value)  # Result : 0 a 1 b 2 c 3 d 4 e

for i in range(len(L)):
    print(i, L[i])   # I think this way should be better :)
