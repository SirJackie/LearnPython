#
# Super() Function can call the Methods from Base Classes
# Format : super(ThisClass, self).BaseClassMethod()
#     or : super().BaseClassMethod()
#

class A(object):
    def MethodInsideA(self):
        print("A is HERE!!!")

class B(A):
    def MethodInsideB(self):
        print("B is HERE!!!")
        super(B, self).MethodInsideA()
        super().MethodInsideA()

b = B()
b.MethodInsideB()
# Result :
# B is HERE!!!
# A is HERE!!!
# A is HERE!!!
