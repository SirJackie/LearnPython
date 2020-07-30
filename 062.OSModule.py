import os

# Get OS Status
print(os.name)     # Result : nt
# print(os.uname)  # Not available in Windows

# Get PATH
print(os.environ)
print(os.environ["PATH"])
print(os.environ.get("PATH"))


#
# Access Folder
#

# Get the Absolutely Path
print(os.path.abspath("."))
# Result : C:\Users\Admin\PycharmProjects\LearnPython

# Join the Path
print(os.path.join("C:\\Users\\Admin\\PycharmProjects\\LearnPython", "Blah"))
# Result : C:\Users\Admin\PycharmProjects\LearnPython\Blah

# Split the Path
print(os.path.split(os.path.abspath(".")))
# Result : ('C:\\Users\\Admin\\PycharmProjects', 'LearnPython')

# Split the Extension
print(os.path.splitext("C:\\Path\\To\\File\\Test.txt"))
# Result : ('C:\\Path\\To\\File\\Test', '.txt')

# Make a New Directory
os.mkdir(os.path.join("C:\\Users\\Admin\\PycharmProjects\\LearnPython", "Blah"))

# Remove a Directory
os.rmdir(os.path.join("C:\\Users\\Admin\\PycharmProjects\\LearnPython", "Blah"))


#
# Access File
#

# Create and Copy a File
with open("C:\\Windows\\System32\\cmd.exe", "rb") as origin:
    with open(".\\cmd.exe", "wb") as f:
        f.write(origin.read())

# Rename a File
os.rename("cmd.exe", "cmd.txt")

# Remove a File
os.remove("cmd.txt")

#
# Use List Comprehension to Filter the Files
#

all_the_folders = [x for x in os.listdir(".") if os.path.isdir(x)]
print(all_the_folders)  # Result : ['.git', '.idea', '__pycache__']

all_the_python_codes = [x for x in os.listdir(".") if os.path.splitext(x)[1] == ".py"]
print(all_the_python_codes)  # Result : ['001.IO.py', ..., 'UnitTestPractice.py']
