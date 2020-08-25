##multilevel inheritance

class A:
    def classA():
        print("im from classA")
class B(A):
    def classB():
        print("im from classB")
class C(B):
    def classC():
        print("im from classC")

obj=C
obj.classB()
obj.classC()
