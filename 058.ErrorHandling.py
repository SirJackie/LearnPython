#
# If there is an Error:
# Order : try(maybe incomplete) -> except (-> finally)
#

try:
    print("try...")
    r = 10 / 0
    print("result : %s" % r)
except ZeroDivisionError as e:
    print("except %s..." % e)
finally:
    print("finally...")

# Result :
# try...
# except division by zero...
# finally...


#
# If there is no Error:
# Order : try (-> finally)
#

try:
    print("try...")
    r = 10 / 2
    print("result : %s" % r)
except ZeroDivisionError as e:
    print("except %s..." % e)
finally:
    print("finally...")

# Result :
# try...
# result : 5.0
# finally...


#
# Complex Error Handling (multi except and else)
#
# else : If the except doesn't runs, the else will be run
#
# If there is an Error:
# try(not complete) -> except(1 or 2) -> finally
#
# If there is no Error:
# try -> else -> finally
#

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')

# Result :
# try...
# result: 5.0
# no error!
# finally...


#
# Remember "except" can also catch the Sub Classes of the Error
#

try:
    a = int("Hello")
except BaseException as e:
    print('BaseException')
except ValueError as e:
    print('ValueError')
# Result : BaseException
# ValueError is a Sub Class of BaseException
# So "except BaseException" will catch the ValueError

try:
    a = int("Hello")
except ValueError as e:
    print('ValueError')
except BaseException as e:
    print('BaseException')
# Result : ValueError
# This is the right way


#
# "except" can also cross multi-functions
#

def foo(s):
    return int(s) / 10

def bar(s):
    return foo(s) * 10

def main():
    try:
        print(bar("Hello World!"))
    except ValueError as e:
        print(e)
    finally:
        print("finally")

main()

# Result :
# invalid literal for int() with base 10: 'Hello World!'
# finally


#
# Use logging to catch the Error , the program can continue running
#

import logging

def foo(s):
    return int(s) / 10

def bar(s):
    return foo(s) * 10

def main():
    try:
        print(bar("Hello World!"))
    except BaseException as e:
        logging.exception(e)

main()
print("END")

# Result :
# ERROR:root:invalid literal for int() with base 10: 'Hello World!'
# Traceback (most recent call last):
#   File "C:/Users/Admin/PycharmProjects/LearnPython/058.ErrorHandling.py", line 136, in main
#     print(bar("Hello World!"))
#   File "C:/Users/Admin/PycharmProjects/LearnPython/058.ErrorHandling.py", line 132, in bar
#     return foo(s) * 10
#   File "C:/Users/Admin/PycharmProjects/LearnPython/058.ErrorHandling.py", line 129, in foo
#     return int(s) / 10
# ValueError: invalid literal for int() with base 10: 'Hello World!'
# END

# The "END" shows that the program was continue running
# even there is an Error


#
# Raise Default Error or your own Error use "raise"
#

class FooError(ValueError):
    pass

def foo(s):
    if not isinstance(s, int):
        raise FooError("Argument is NOT a INT!!!")
        # raise ValueError("Argument is NOT a INT!!!")
try:
    foo("blah")
except FooError as e:
    print("FooError")

# Result : FooError


#
# Raise an Error to Python use "raise" with nothing
#

try:
    foo("blah")
except FooError as e:
    print("FooError")
    raise

# Result :
# FooError
# ValueError: invalid literal for int() with base 10: 'Hello World!'
# Traceback (most recent call last):
#   File "C:/Users/Admin/PycharmProjects/LearnPython/058.ErrorHandling.py", line 183, in <module>
#     foo("blah")
#   File "C:/Users/Admin/PycharmProjects/LearnPython/058.ErrorHandling.py", line 168, in foo
#     raise FooError("Argument is NOT a INT!!!")
# __main__.FooError: Argument is NOT a INT!!!
