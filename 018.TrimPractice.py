def trim(s):
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s


# Test:
if trim('hello  ') != 'hello':
    print('Rejected')
elif trim('  hello') != 'hello':
    print('Rejected')
elif trim('  hello  ') != 'hello':
    print('Rejected')
elif trim('  hello  world  ') != 'hello  world':
    print('Rejected')
elif trim('') != '':
    print('Rejected')
elif trim('    ') != '':
    print('Rejected')
else:
    print('Accepted')
