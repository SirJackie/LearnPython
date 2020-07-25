#
# Couple of things about Functions's __name__
#

def now():
    print("2020-7-25")

f = now

print(now)  # Result : <function now at 0x000001B829A085E8>
print(f)    # Result : <function now at 0x000001B829A085E8>

print(now.__name__)  # Result : now
print(f.__name__)    # Result : now


#
# Define a Decorator
#

def log(func):
    def wrapper(*args, **kw):
        print("Call %s:" % func.__name__)
        print("Begin!")
        returnValue = func(*args, **kw)
        print("End!")
        return returnValue
    return wrapper


#
# Use the Decorator
#

@log
def now():
    print("2020-7-25")
# <@log> works the same as <now = log(now)>

now()
# Result :
# Call now:
# Begin!
# 2020-7-25
# End!


#
# Decorator with Arguments
#

def log(text="Call"):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s" % (text, func.__name__))
            print("Begin!")
            returnValue = func(*args, **kw)
            print("End!")
            return returnValue
        return wrapper
    return decorator

@log()
def now():
    print("2020-7-25")

now()
# Result :
# Call now:
# Begin!
# 2020-7-25
# End!

@log("Execute")
def now():
    print("2020-7-25")
# <@log("Execute")> works the same as <now = log("Execute")(now)>

now()
# Result :
# Execute now
# Begin!
# 2020-7-25
# End!


#
# One More Question
#

print(now.__name__)  # Expected : now , Result : wrapper

# This is because the Decorator
# Use THIS WAY to write a Decorator with no __name__ effect:

import functools

def log(text="Call"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s" % (text, func.__name__))
            print("Begin!")
            returnValue = func(*args, **kw)
            print("End!")
            return returnValue
        return wrapper
    return decorator

@log("Execute")
def now():
    print("2020-7-25")

print(now.__name__)  # Expected : now , Result : now
