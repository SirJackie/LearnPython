#
# List
#

# Define the List

classmates = ["Michael", "Bob", "Tracy"]
print(classmates)  # ['Michael', 'Bob', 'Tracy']
print(len(classmates))  # 3


# Read the List

print(classmates[0])   # Michael
print(classmates[1])   # Bob
print(classmates[2])   # Tracy
# print(classmates[3])   # Error!

print(classmates[-1])  # Tracy
print(classmates[-2])  # Bob
print(classmates[-3])  # Michael
# print(classmates[-4])  # Error!


# Add Things to List

print(classmates)  # ['Michael', 'Bob', 'Tracy']
classmates.append("Adam")
print(classmates)  # ['Michael', 'Bob', 'Tracy', 'Adam']
classmates.insert(1, "Jack")
print(classmates)  # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']


# Delete Things from List

print(classmates)  # ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
classmates.pop()
print(classmates)  # ['Michael', 'Jack', 'Bob', 'Tracy']
classmates.pop(1)
print(classmates)  # ['Michael', 'Bob', 'Tracy']


# Modify the List

classmates[0] = "Man"
print(classmates)  # ['Man', 'Bob', 'Tracy']


# Features About the List

list1 = ["Apple", 123, True]   # Different Types of Variables can be in one List
list2 = ["Apple", [1, 2], 1]   # One List can be in Another List
list3 = []                     # Empty List can be defined



#
# Tuple is a immutable List
#

# Define Tuple

numbers = (1, 2, 3)
print(numbers)  # (1, 2, 3)


# Read Tuple

print(numbers[0])   # 1
print(numbers[-1])  # 3

# You can't modify a tuple


# Features About Tuple

one = (1)    # one is a int number
print(one)   # Result : 1

oneT = (1,)  # oneT is a tuple included int number 1
print(oneT)  # Result : (1,)
