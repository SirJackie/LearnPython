#
# Dict
#

# Define the Dict (Dict = {key: value, key: value})
d = {"Michael": 95,
     "Bob": 75,
     "Tracy": 85}

# Read the Value
print(d["Michael"])  # Result : 95

# Write or Replace the Value
d["Michael"] = 100
d["Adam"] = 60
print(d)  # Result : {'Michael': 100, 'Bob': 75, 'Tracy': 85, 'Adam': 60}

# Test if the Dict have this Key
print("Michael" in d)    # Result : True
print("John" in d)       # Result : False
print(d.get("Michael"))  # Result : 100
print(d.get("John"))     # Result : None
print(d.get("John", 5))  # Result : 5 (Your custom error message)

# Delete Key From the Dict
d.pop("Adam")
print(d)       # Result : {'Michael': 100, 'Bob': 75, 'Tracy': 85}
d.pop("Bob")
print(d)       # Result : {'Michael': 100, 'Tracy': 85}

# Key Must Be an Unchangeable Variable (not list and so on)


#
# Set
#

# Define the Set (  Set = {...} or Set = set([list])  )
s = {1, 2, 3}
print(s)  # Result : {1, 2, 3}
s = {1, 1, 1, 2, 3, 3}  # Set does not have any duplicate elements
print(s)  # Result : {1, 2, 3}

# Modify the Set
s.add(4)
print(s)  # Result : {1, 2, 3, 4}
s.remove(4)
print(s)  # Result : {1, 2, 3}

# Calculate the Set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # Result : {2, 3}
print(s1 | s2)  # Result : {1, 2, 3, 4}


#
# Things about Unchangeable Variable
#

l = [1, 2, 3, 4]     # List is a Changeable Variable
s = "abc"            # String is not a Changeable Variable
s.replace('a', "A")  # But this method seems to make string changeable! What's wrong?

print(s)  # Result : abc, this result tells us that string hasn't been changed.
print(s.replace('a', "A"))  # Result : Abc, it tells us return value has been changed.

# replace() method only changed the return value
# All the method of an Unchangeable Variable works the same
# This makes the string an Unchangeable Variable

tup1 = (1, 2, 3)
tup2 = (1, [2, 3])
d[tup1] = 1
# d[tup2] = 2  # Error!!! Tuple includes List is not a Unchangeable Variable
