#
# Inheritance
#

class Animal(object):
    def run(self):
        print("Animal is Running")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()
d.run()  # Result : Animal is Running
c.run()  # Result : Animal is Running

# This is because Dog and Cat Inherit Animal's Methods


#
# Polymorphism
#

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

d = Dog()
c = Cat()
d.run()  # Result : Dog is running
c.run()  # Result : Cat is running

# This is because d.run() will execute Dog.run() first instead of Animal.run()
# This is what Polymorphism is


#
# Relation Between Superclass and Subclass
#

animal1 = Animal()
dog1 = Dog()

# Dog is Animal (Subclass is a kind of Superclass)
print(isinstance(dog1, Animal))     # Result : True
print(isinstance(dog1, Dog))        # Result : True

# Animal isn't Dog (Superclass isn't a kind of Subclass)
print(isinstance(animal1, Animal))  # Result : True
print(isinstance(animal1, Dog))     # Result : False
