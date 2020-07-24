# Create normalize() function to format the username like this:
# ['Adam', 'Lisa', 'Bart']

def normalize(x):
    x = x.lower()
    firstChar = ord(x[0])
    firstChar = firstChar - 32
    x = chr(firstChar) + x[1:]
    return x

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)  # Result : ['Adam', 'Lisa', 'Bart']
