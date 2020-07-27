#
# @Property can create Virtual Properties (Actually Functions)
#

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    # Create Virtual Property "score" 's Reading Method
    @property
    def score(self):
        return "%s\'s Score Is : %d Points" % (self.name, self.__score)

    # Create Virtual Property "score" 's Writing Method
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score Must Be A INT!!!")
        if value < 0 or value > 100:
            raise ValueError("Score Must Between 0-100")
        self.__score = value


a = Student("Micheal", 90)

# Access Virtual Property
print(a.score)      # Result : Micheal's Score Is : 90 Points
# a.score = "Blah"  # ValueError: Score Must Be A INT!!!
# a.score = 999999  # Result : ValueError: Score Must Between 0-100
a.score = 99        # Pass!
