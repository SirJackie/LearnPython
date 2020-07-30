#
# Read File
#

# Use Open to Read a File
f = open(".\\test.txt", "r")
print(f.read())
f.close()

# File IO can be Error at any time
# So Remember to use try...finally... to catch the error
# And Remember to f.close() , or there will be an serious Error
try:
    f = open(".\\test.txt", "r")
    print(f.read())
finally:
    if f:
        f.close()

# If you think try...finally... is too complex
# use "with" statement Instead!
with open(".\\test.txt") as f:
    print(f.read())

# Some methods
# Use f.read(size) to read part of the file (can't find the end)
# Use f.readline() to read a line once      (can't find the end)
# use f.readlines() to read all lines to a list
with open(".\\test.txt") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line.strip())


#
# Read Binary File
#

with open("C:\\Windows\\System32\\cmd.exe", "rb") as f:
    print(f.read())
    # Result : b'MZ\x90\x00\x03\x00...'


#
# Read Custom Encoding File
#

with open(".\\TestWithUTF-8.txt", "r", encoding="UTF-8", errors="ignore") as f:
    print(f.read())
    # Result :你好  # 世界


#
# Write File
#

with open(".\\Test.txt", "w") as f:
    f.write("Hello World!\nLine2\nLine Three")

#
# Write Binary File
#

with open(".\\cmd.exe", "wb") as f:
    with open("C:\\Windows\\System32\\cmd.exe", "rb") as origin:
        f.write(origin.read())

#
# Write Custom Encoding File
#

with open(".\\TestWithUTF-8.txt", "w", encoding="UTF-8", errors="ignore") as f:
    f.write("你好\n世界")


#
# Append Things at the end of the File
#

with open(".\\Test.txt", "a") as f:
    f.write("\nAppend Things!")
