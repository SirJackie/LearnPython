#
# List Comprehension
# Format : [rule-of-x for x in range() <if x-do-sth == True>]
#

comp1 = [x * 5 for x in range(1, 6)]
print(comp1)  # Result : [5, 10, 15, 20, 25]

comp2 = [x * x for x in range(1, 11)]
print(comp2)  # Result : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

comp3 = [x * x for x in range(1,11) if x % 2 == 0]
print(comp3)  # Result : [4, 16, 36, 64, 100]

comp4 = [m + n for m in "ABC" for n in "XYZ"]
print(comp4)  # Result : ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

comp5 = [k + "=" + str(v) for k, v in {"a": 1, "b": 2}.items()]
print(comp5)  # Result : ['a=1', 'b=2']

comp6 = [s.lower() for s in ["STRING1", "String2", "sTRING3"]]
print(comp6)  # Result : ['string1', 'string2', 'string3']

comp7 = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(comp7)  # Result : [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# List Comprehension can simplify the codes
import os
listOfFiles = [d for d in os.listdir(".")]
print(listOfFiles)
