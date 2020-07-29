#
# Couple of things about type of Instance and Class
#

class Student(object):
    pass

s = Student()
print(type(s))  # Result : <class '__main__.Student'>
# "s" instance is a instance of class "Student"
# So "s" 's type is "Student"

print(type(Student))  # Result : <class 'type'>
# "Student" class is a "instance" of metaclass "type"
# So "Student" 's type is "type"


#
# "type" is a metaclass built-in in Python
# All the objects are inherit from metaclass "type"
# Here are the examples:
#

# Object "String" is a instance of Class "str"
# Or we can say Object "String" is inherit from Class "str"
print("String".__class__)  # Result : <class 'str'>

# Class "str" is a "instance" of Metaclass "type"
# Or we can say Class "str" is inherit from Metaclass "type"
print("String".__class__.__class__)  # Result : <class 'type'>


#
# Because "type" is a Metaclass,
# You can build class using "type()" calling
#

def CustomInit(self, Property1, Property2):
    self.Property1 = Property1
    self.Property2 = Property2

def CustomMethod(self):
    print(self.Property1, self.Property2)

NewClass = type("NewClass",  # New Class' Name
                (object,),   # Inheritance Classes
                {            # A Dict including Properties and Methods
                    "Property1": None,
                    "Property2": None,
                    "__init__": CustomInit,
                    "Method": CustomMethod
                })

# NewClass created by "type()" works the same as Normal Classes
# Actually Normal Classes are created by "type()" automatically
print(NewClass)        # Result : <class '__main__.NewClass'>
print(type(NewClass))  # Result : <class 'type'>
instance1 = NewClass(123, "String")
instance1.Method()     # Result : 123 String


#
# "type" is a built-in Metaclass
# Instead of using "type", you can created your own Metaclass
# by inherit your class from "type"
#

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value: self.append(value)
        return type(name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

list1 = []
list2 = MyList()

# list1.add(1)  # AttributeError: 'list' object has no attribute 'add'
list2.add(1)

print(list1)  # Result : []
print(list2)  # Result : [1]
# So Now instances created by "MyList" class have the attribute "add"
