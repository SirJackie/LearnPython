def hanoi(n, a, b, c, carrier=[1]):
    if n == 1:
        print("Step", carrier[0], a, "=>", c)
        carrier[0] = carrier[0] + 1
        return
    hanoi(n-1, a, c, b)
    print("Step", carrier[0], a, "=>", c)
    carrier[0] = carrier[0] + 1
    hanoi(n-1, b, a, c)

hanoi(10, "A", "B", "C")