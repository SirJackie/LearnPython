# Int() support base=2 option
x = int("00101010", base=2)
y = int("10000000", base=2)
z = int("11111111", base=2)
print(x, y, z)  # Result : 42 128 255

# You can use Default Argument to omit it
def int2(s):
    return int(s, base=2)
x = int2("00101010")
y = int2("10000000")
z = int2("11111111")
print(x, y, z)  # Result : 42 128 255

# Or you can use Partial Function to omit it
import functools
int2 = functools.partial(int, base=2)
x = int2("00101010")
y = int2("10000000")
z = int2("11111111")
print(x, y, z)  # Result : 42 128 255
