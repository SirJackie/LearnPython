#
# __slots__ can ban the Illegal Property Adding
#

class Student(object):
    __slots__ = ("name", "age")
    # Only allow to add "name" and "age" property

a = Student()
a.name = "Michael"
a.age = 20
# a.score = 100  # AttributeError: 'Student' object has no attribute 'score'


#
# __slots__ doesn't make effect to Subclasses
#

class GraduatedStudent(Student):
    pass

b = GraduatedStudent()
b.score = 999


#
# If the Subclasses use __slots__ , SuperClass's __slots__ will still makes effect
#

class GraduatedStudent(Student):
    __slots__ = ("score", )

c = GraduatedStudent()
c.score = 999
c.name = "John"
