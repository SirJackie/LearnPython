class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

# Test:
if Student.count != 0:
    print('Rejected')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('Rejected')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('Rejected')
        else:
            print('Students:', Student.count)
            print('Accepted')
