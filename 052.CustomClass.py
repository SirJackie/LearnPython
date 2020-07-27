#
# __str(), __repr__() and __len()
#

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student %s" % self.name

    __repr__ = __str__  # For Python Interactive Environment

    def __len__(self):
        return 100000000000000

m = Student("Micheal")
print(m)       # Result : Student Micheal
print(len(m))  # Result : 100000000000000


#
# __iter__() and __next() for Iteration
#

class Fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)


#
# __getitem__() for Indexing
#

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

print(Fib()[0])      # Result : 1
print(Fib()[1])      # Result : 1
print(Fib()[2])      # Result : 2
print(Fib()[3])      # Result : 3
# print(Fib()[0:3])  # Error!

# __getitem__ with Slice

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            L = []
            a, b = 1, 1
            for x in range(stop):
                a, b = b, a + b
                if x >= start:
                    L.append(a)
            return L

print(Fib()[0])    # Result : 1
print(Fib()[1])    # Result : 1
print(Fib()[2])    # Result : 2
print(Fib()[3])    # Result : 3
print(Fib()[0:3])  # Result : [1, 2, 3]
print(Fib()[:10])  # Result : [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
