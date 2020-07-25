"MyModule is a testing module."

__author__ = "SirJackie"

import sys

def Merger(s="", mode="Merge", carrier=["Hello, "]):
    if mode == "Merge":
        carrier[0] = carrier[0] + s + " "
    elif mode == "GetValue":
        return carrier[0]

def test():
    args = sys.argv
    if len(args) <= 1:
        print("Hello, World!")
    else:
        for s in args[1:]:
            Merger(s)
        print(Merger(mode="GetValue"))

if __name__ == "__main__":
    test()
