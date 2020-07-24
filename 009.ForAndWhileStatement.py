#
# For Statement
#


# for i in list/tuple

names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)
# Result : Michael Bob Tracy


# for i in range()

for i in range(5):  # the same as for i in [0, 1, 2, 3, 4]
    print(i)
# Result : 0 1 2 3 4


#
# While Statement
#


n = 10
while n >= 0:
    print(n)
    n = n - 1
# Result : 10 9 8 7 6 5 4 3 2 1 0
