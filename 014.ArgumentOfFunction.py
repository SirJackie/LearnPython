#
# Positional Argument
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
# Changeable Argument (arguments become tuple using *)
#
def Calc(*numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum

# All the Arguments become a tuple call "numbers", this is what *numbers do
print(Calc(1, 2, 3))     # Result : 14
print(Calc(1, 3, 5, 7))  # Result : 84

# You can use *list to make a list become Changeable Arguments
numlist = [1, 3, 5, 7]
print(Calc(*numlist))    # Result : 84

# *[1, 2, 3] => 1, 2, 3  (List becomes Changeable Arguments)
# *1, 2, 3 => (1, 2, 3)  (Changeable Arguments become Tuple)
# So the * in Python doesn't mean pointer, it mean Changeable Arguments


#
# Key Word Argument (arguments become dict using **)
#
def Report(name, age, **kw):
    print(name, age, kw)

# All the Arguments become a dict call "kw", this is what **kw do
Report("Michael", 30)                    # Result : Michael 30 {}
Report("Michael", 30, city="Beijing")    # Result : Michael 30 {'city': 'Beijing'}
Report("Michael", 30, k1="w1", k2="w2")  # Result : Michael 30 {'k1': 'w1', 'k2': 'w2'}

# You can use **kwdict to make a dict become Key Word Arguments
kwdict = {"k1": "w1", "k2": "w2"}
Report("Michael", 30, **kwdict)          # Result : Michael 30 {'k1': 'w1', 'k2': 'w2'}

# *{"k1": "w1", "k2": "w2"} => k1="w1", k2="w2"  (Dict becomes Key Word Arguments)
# *k1="w1", k2="w2" => {"k1": "w1", "k2": "w2"}  (Key Word Arguments becomes Dict)
# So the ** in Python doesn't mean pointer of pointer, it mean Key Word Arguments
