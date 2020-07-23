import math


# Quadratic calculates the solution of ax² + bx + c = 0
def Quadratic(a, b, c):
    delta = b * b - 4 * a * c  # b²-4ac
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


solution = Quadratic(2, 3, 1)
print(solution)
