class Animal(object):
    def run(self):
        print("Animal is Running")

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

def f():
    pass


#
# Type() Function
#

# Get Basic Variable's Type
print(type(123))    # Result : <class 'int'>
print(type("str"))  # Result : <class 'str'>
print(type(None))   # Result : <class 'NoneType'>

# Get Function's Type
print(type(f))      # Result : <class 'function'>
print(type(abs))    # Result : <class 'builtin_function_or_method'>

# Get Object's Type
print(type(a))      # Result : <class '__main__.Animal'>
print(type(d))      # Result : <class '__main__.Dog'>
print(type(h))      # Result : <class '__main__.Husky'>

# Judge if two Variables are the same type
print(type(123) == int)    # Result : True
print(type(123) == str)    # Result : False
print(type("str") == str)  # Result : True

# Judge Function's Type
import types
print(type(f) == types.FunctionType)             # Result : True
print(type(abs) == types.BuiltinFunctionType)    # Result : True
print(type(a) == Animal)                         # Result : True
print(type(lambda x: x) == types.LambdaType)     # Result : True
print(type((x for x in range(10))) == types.GeneratorType)
                                                 # Result : True


#
# Isinstance() Function
#

# Type() can't judge the Inheritance Relation
print(type(h) == Husky)         # Result : True
print(type(h) == Dog)           # Result : False

# But Isinstance() can do so
print(isinstance(h, Husky))     # Result : True
print(isinstance(h, Dog))       # Result : True

# Isinstance() can also judge Variable's Type!
print(isinstance(123, int))     # Result : True
print(isinstance("str", str))   # Result : True
print(isinstance(b'a', bytes))  # Result : True

# Isinstance() can even judge if variable are one of the some types
print(isinstance(123, (int, str)))    # Result : True
print(isinstance("str", (int, str)))  # Result : True


#
# Dir() Function
# Get All the Properties and Methods of this Object
#

print(dir("ABC"))  # Result : ['__add__', ..., '__len__',  ..., 'zfill']

# Something about __len__() Method
print(len("ABC"))       # Result : 3
print("ABC".__len__())  # Result : 3

# len() function is actually calling sth.__len__()
class MyObject(object):
    def __len__(self):
        return 100
obj = MyObject()
print(len(obj))  # Result : 100


#
# hasattr(), getattr() and setattr()
#

print(hasattr(obj, "__len__"))  # Result : True
setattr(obj, "__len__", 100)
print(getattr(obj, "__len__"))  # Result : 100

# print(getattr(obj, "x"))
# Result : AttributeError: 'MyObject' object has no attribute 'x'

# Custom Error Message
print(getattr(obj, "x", 404))   # Result : 404
