from functools import reduce

def str2num(s):
    # return int(s)  # BUG IS HERE!!!
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


#
# Before Fixing:
#

# 100 + 200 + 345 = 645
# Traceback (most recent call last):
#   File "C:/Users/Admin/PycharmProjects/LearnPython/059.BugFixPractice.py", line 18, in <module>
#     main()
#   File "C:/Users/Admin/PycharmProjects/LearnPython/059.BugFixPractice.py", line 15, in main
#     r = calc('99 + 88 + 7.6')
#   File "C:/Users/Admin/PycharmProjects/LearnPython/059.BugFixPractice.py", line 10, in calc
#     return reduce(lambda acc, x: acc + x, ns)
#   File "C:/Users/Admin/PycharmProjects/LearnPython/059.BugFixPractice.py", line 4, in str2num
#     return int(s)
# ValueError: invalid literal for int() with base 10: ' 7.6'


#
# After Fixing :
#

# 100 + 200 + 345 = 645.0
# 99 + 88 + 7.6 = 194.6
