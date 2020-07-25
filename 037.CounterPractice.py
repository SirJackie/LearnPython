def CreateCounter(init):
    def Counter(i, init=[init]):
        init[0] = init[0] + i
        return init[0]
    return Counter

f1 = CreateCounter(5)
print(f1(2))  # Result : 7
print(f1(3))  # Result : 10

f2 = CreateCounter(105)
print(f2(2))  # Result : 107
print(f2(3))  # Result : 110

print(f1(5))  # Result : 15
print(f2(5))  # Result : 115

# f1 and f2 are independent!
