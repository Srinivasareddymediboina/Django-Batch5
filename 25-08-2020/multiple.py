### multiple inheritance
class A:
    def classA():
        print("im from classA")
class B():
    def classB():
        print("im from classB")
class C(A,B):
    def classC():
        print("im from classC")

obj=C
obj.classA()
obj.classB()
obj.classC()
