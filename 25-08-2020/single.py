###single level inheritance

class classA:
    a,b=10,20
    def display():
        print("im from classA")

class classB(classA):
    c,d=7,8
    def show():
        print("im from classB")


obj=classB
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

obj.display()
obj.show()
