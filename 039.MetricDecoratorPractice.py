import time, functools
def metric(fn):
    def wrapper(*args, **kw):
        startingTime = time.time()
        returnValue = fn(*args, **kw)
        endingTime = time.time()
        runningTime = (endingTime - startingTime) * 1000
        print('%s executed in %s ms' % (fn.__name__, runningTime))
        return returnValue
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print("Rejected")
elif s != 7986:
    print("Rejected")
else:
    print("Accepted")
