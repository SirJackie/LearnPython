class Student(object):
    name = "Student"    # Class Property, shared by different Instance

    def __init__(self, age):
        self.age = age  # Instance Property, owned by single Instance


a = Student(10)
b = Student(15)

print(a.name)  # Result : Student , Class Property
print(a.age)   # Result : 10 , Instance Property
print(b.name)  # Result : Student , Class Property
print(b.age)   # Result : 15 , Instance Property

# Use Instance Property to Cover Class Property (NOT RECOMMENDED)
a.name = "Student A"
print(a.name)        # Result : Student A , Instance Property
print(b.name)        # Result : Student   , Class Property
print(Student.name)  # Result : Student   , Class Property

# When Instance Property gone, the Class Property can be access again
del a.name
print(a.name)        # Result : Student

# Use Class.Property to access Class Property
Student.name = "BlahBlah"
print(a.name)  # Result : BlahBlah
print(b.name)  # Result : BlahBlah
