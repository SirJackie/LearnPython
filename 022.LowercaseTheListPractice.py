# L1 is a list including Strings and Other things
# Please create L2 with List Comprehension
# To make sure L2 only included all the strings in L1 with lowercase

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# Test:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('Accepted')
else:
    print('Rejected')
