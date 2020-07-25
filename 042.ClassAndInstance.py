#
# Create a Class
#

class Student(object):
    pass

bart = Student()
print(bart)  # Result : <__main__.Student object at 0x000001E9956ADC48>


#
# Create Property for a Instance
#

bart.name = "Bart Simpson"
print(bart.name)  # Result : Bart Simpson


#
# Create Property for a Class
#

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student("Bart Simpson", 59)
print(bart.name)   # Result : Bart Simpson
print(bart.score)  # Result : 59


#
# Create Method for a Class
#

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def PrintScore(self):
        print("%s: %s" % (self.name, self.score))

bart = Student("Bart Simpson", 59)
bart.PrintScore()  # Result : Bart Simpson: 59
