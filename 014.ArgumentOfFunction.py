#
# Positional Arguments
#
def pow(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(pow(10, 3))









#
# Default Argument (arg=defaultValue)
#
def Report(name, age, grade="A", city="Beijing"):
    print(name, age, grade, city)

Report("XiaoMing", 10)                            # Result : XiaoMing 10 A Beijing
Report("LiErGou", 10, "F")                        # Result : LiErGou 10 F Beijing
Report("Charlie", 10, city="London")              # Result : Charlie 10 A London
Report("Michael", 25, city="TianJin", grade="S")  # Result : Michael 25 S TianJin

# A Little Bug about Default Argument
def AddEnd(l=[]):
    l.append("END")
    return l

print(AddEnd(["Michael", "John"]))  # Result : ['Michael', 'John', 'END']
print(AddEnd())                     # Result : ['END']
print(AddEnd())                     # Result : ['END', 'END'], It's a BUG!!!

# Default Argument must be an Unchangeable Variable
def AddEnd(l=None):
    if l is None:
        l = []
    l.append("END")
    return l

print(AddEnd(["Michael", "John"]))  # Result : ['Michael', 'John', 'END']
print(AddEnd())                     # Result : ['END']
print(AddEnd())                     # Result : ['END'], BUG SOLVED!










#
# Formal Arguments (arguments become tuple using *)
#
def Calc(*numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum

# All the Arguments become a tuple call "numbers", this is what *numbers do
print(Calc(1, 2, 3))     # Result : 14
print(Calc(1, 3, 5, 7))  # Result : 84

# You can use *list to make a list become Formal Arguments
numlist = [1, 3, 5, 7]
print(Calc(*numlist))    # Result : 84

# *[1, 2, 3] => 1, 2, 3  (List becomes Formal Arguments)
# *1, 2, 3 => (1, 2, 3)  (Formal Arguments become Tuple)
# So the * in Python doesn't mean pointer, it mean Formal Arguments










#
# Keyword Arguments (arguments become dict using **)
#
def Report(name, age, **kw):
    print(name, age, kw)

# All the Arguments become a dict call "kw", this is what **kw do
Report("Michael", 30)                    # Result : Michael 30 {}
Report("Michael", 30, city="Beijing")    # Result : Michael 30 {'city': 'Beijing'}
Report("Michael", 30, k1="w1", k2="w2")  # Result : Michael 30 {'k1':'w1','k2':'w2'}

# You can use **kwdict to make a dict become Key Word Arguments
kwdict = {"k1": "w1", "k2": "w2"}
Report("Michael", 30, **kwdict)          # Result : Michael 30 {'k1':'w1','k2':'w2'}

# *{"k1": "w1", "k2": "w2"} => k1="w1", k2="w2"  (Dict becomes Keyword Arguments)
# *k1="w1", k2="w2" => {"k1": "w1", "k2": "w2"}  (Keyword Arguments becomes Dict)
# So the ** in Python doesn't mean pointer of pointer, it mean Keyword Arguments












#
# Named Keyword Arguments
#
def Report(name, age, *, city, job):  # before * are Positional Arguments
    print(name, age, city, job)       # after * are Named Keyword Arguments

# Named Keyword Argument must be given as key-value pairs
Report("Michael", 30, city="Beijing", job="Programmer")

# If you don't do so, it will be an Error!
# Report("Micheal", 30, "Beijing", "Programmer")  # Error!!!
# TypeError: Report() takes 2 positional arguments but 4 were given

def Report(name, age, *args, city, job):  # *args works the same as *
    print(name, age, args, city, job)     # that means Formal Arguments == *

Report("Micheal", 30, "arg1", "arg2", city="Beijing", job="Programmer")
# Result : Micheal 30 ('arg1', 'arg2') Beijing Programmer


#
# Use all 5 kinds of Arguments
# Priority :             Positional Arguments
#         =>     Default Positional Arguments
#         =>                 Formal Arguments
#         =>          Named Keyword Arguments
#         =>  Default Named Keyword Arguments
#         =>                Keyword Arguments
#

def ArgMsg(a, b=10, *args, c, d=10, **kw):
    print(a, b, args, c, d, kw)
    # a    is             Positional Argument
    # b    is     Default Positional Argument
    # args is                 Formal Argument
    # c    is          Named Keyword Argument
    # d    is  Default Named Keyword Argument
    # kw   is                Keyword Argument

ArgMsg(1, 2, "tup1", "tup2", c=3, d=4, dict1=1, dict2=2)
# Result : 1 2 ('tup1', 'tup2') 3 4 {'dict1': 1, 'dict2': 2}


#
# You can use a tuple and a dict to call any kinds of function
#

args = (1, 2, "tup1", "tup2")
kw = {"c": 3, "d": 4, "dict1": 1, "dict2": 2}
ArgMsg(*args, **kw)
# Result : 1 2 ('tup1', 'tup2') 3 4 {'dict1': 1, 'dict2': 2}

# It works like this:
#    ArgMsg(*args, **kw)
# => ArgMsg(*(1, 2, "tup1", "tup2"), **{"c": 3, "d": 4, "dict1": 1, "dict2": 2})
# => ArgMsg(1, 2, "tup1", "tup2", c=3, d=4, dict1=1, dict2=2)
