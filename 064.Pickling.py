#
# Pickling use pickle
#

import pickle
d = {"Name": "Michael", "Job": "Programmer", "Age": 25}

# Use pickle.dumps() to pickling an object to bytes
bytes = pickle.dumps(d)
print(bytes)                      # Result : b'\x80\x03}...\x05K\x19u.'

# Use pickle.loads() to unpickling an object from bytes
print(pickle.loads(bytes))        # Result: {'Name': 'Michael'...}

# Use pickle.dump() to pickling an object to file
with open("Pickle.txt", "wb") as f:
    pickle.dump(d, f)             # Output : €}q...erqX   AgeqKu.

# Use pickle.load() to unpickling an object from file
with open("Pickle.txt", "rb") as f:
    print(pickle.load(f))         # Result : {'Name': 'Michael'...}


#
# Pickling use JSON
#

import json

# Use json.dumps() to pickling an object to string
string = json.dumps(d)
print(string)                     # Result : {"Name": "Michael"...}

# Use json.loads() to unpickling an object from string
print(json.loads(string))         # Result : {'Name': 'Michael'...}

# Use json.dumps() and open() to pickling an object to file
with open("PickleWithJSON.txt", "w") as f:
    f.write(json.dumps(d))

# Use json.loads() and open() to unpickling an object from file
with open("PickleWithJSON.txt", "r") as f:
    print(json.loads(f.read()))   # Result : {'Name': 'Michael'...}


#
# Pickling a Class with JSON
#

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Michael", 25)

# You can't directory dumps a Class with json.dumps()
# print(json.dumps(s))  # Result : TypeError

def student2dict(std):
    return {
        "name": std.name,
        "age": std.age
    }

# Use Custom "default" Argument to pickling a Class
string = json.dumps(s, default=student2dict)  # Result : {"name": "Michael"...}
print(string)

# More simple way
print(json.dumps(s, default=lambda std: std.__dict__))  # Same Result

def dict2student(d):
    return Student(d["name"], d["age"])

# Use Custom "object_hook" Argument to unpickling a Class
print(json.loads(string, object_hook=dict2student))
# Result : <__main__.Student object at 0x000002BAA4897908>


#
# Use "ensure_ascii" to make sure there are only ASCII on the string
#

obj = dict(name='小明', age=20)
print(json.dumps(obj, ensure_ascii=True))
# Result : {"name": "\u5c0f\u660e", "age": 20}
# Unicode string was been converted to ASCII-only string
