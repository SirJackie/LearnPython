def is_palindrome(n):
    stringAfterProcess = ""
    for ch in str(n):
        stringAfterProcess = ch + stringAfterProcess

    if stringAfterProcess == str(n):
        return True
    else:
        return False

# Test:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('Accepted')
else:
    print('Rejected')
