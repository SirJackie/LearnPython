#
# Iterable : work with For Statement,   not Lazy Evaluation
# Iterator : work with next() function,     Lazy Evaluation
#

from collections import Iterable, Iterator

Int = 123
List = [1, 2, 3]
Dict = {"a": 1, "b": 2}
String = "Alphabet"
Generator = (x * x for x in range(1, 11))

# All Variables can work with For Statement are Iterable
print(isinstance(Int, Iterable))        # Result : False
print(isinstance(List, Iterable))       # Result : True
print(isinstance(Dict, Iterable))       # Result : True
print(isinstance(String, Iterable))     # Result : True
print(isinstance(Generator, Iterable))  # Result : True

# All Variables can work with next() are Iterator
print(isinstance(Int, Iterator))        # Result : False
print(isinstance(List, Iterator))       # Result : False
print(isinstance(Dict, Iterator))       # Result : False
print(isinstance(String, Iterator))     # Result : False
print(isinstance(Generator, Iterator))  # Result : True

# Use iter() to convert Iterable Variables into Iterators
print(isinstance(iter(List), Iterator))       # Result : False
print(isinstance(iter(Dict), Iterator))       # Result : False
print(isinstance(iter(String), Iterator))     # Result : False
print(isinstance(iter(Generator), Iterator))  # Result : True
