#
# Write StringIO
#

from io import StringIO
f = StringIO()
f.write("Hello")
f.write(" ")
f.write("World")
f.write("!")
print(f.getvalue())


#
# Read StringIO
#

f = StringIO("Hello\nWorld\nBlah")
print(f.readlines())  # Result : ['Hello\n', 'World\n', 'Blah']


#
# Write BytesIO
#

from io import BytesIO
f = BytesIO()
f.write("中文".encode("UTF-8"))
print(f.getvalue())  # Result : b'\xe4\xb8\xad\xe6\x96\x87'


#
# Read BytesIO
#

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())  # Result : b'\xe4\xb8\xad\xe6\x96\x87'
