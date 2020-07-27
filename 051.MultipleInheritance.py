class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("Flying...")

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

d = Dog()
b = Bat()
p = Parrot()
o = Ostrich()

# Dog Inherit Both Mammal and Runnable Class
# This is what Multiple Inheritance Is!
# It also called MixIn
print(isinstance(d, Mammal))    # Result : True
print(isinstance(d, Runnable))  # Result : True
