import re


def is_valid_email(addr):
    return re.match(r"[\w.]+@\w+.\w+", addr)

# Test:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addr):
    result = re.match(r"\w+", addr)
    if result:
        return result.group(0)

    result = re.match(r"<[\w\s]+>", addr)
    if result:
        return result.group(0)[1:-1]

    return None

# Test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
