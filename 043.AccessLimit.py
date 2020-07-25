class Student(object):
    def __init__(self, name, score):
        self.name = name       # Public Property
        self.__score = score   # Private Property

    def GetName(self):
        return self.name

    def GetScore(self):
        return self.__score

    def SetName(self, name):
        self.name = name

    def SetScore(self, score):
        self.__score = score

bart = Student("Bart Simpson", 59)


#
# Access Public Property
#

# Read
print(bart.name)         # Result : Bart Simpson
print(bart.GetName())    # Result : Bart Simpson

# Write
bart.name = "Bart Blah"  # Change a Public Property
print(bart.name)         # Result : Bart Blah
print(bart.GetName())    # Result : Bart Blah


#
# Access Private Property
#

# Read
# print(bart.__score)    # Error!!! Can't Access a Private Property
print(bart.GetScore())   # Result : 59

# Write
bart.__score = 100       # Change a Private Property
print(bart.__score)      # Result : 100 , seems to be changed?
print(bart.GetScore())   # Result : 59  , actually not been changed!

# This is because bart.__score isn't the bart.__score inside Class :)
