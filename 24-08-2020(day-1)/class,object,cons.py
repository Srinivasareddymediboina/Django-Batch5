Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Hi:
	a=10
	b=20
	def display():
		print("hi students welcome to django session")

		
>>> Hi.a
10
>>> Hi.display()
hi students welcome to django session
>>> obj=Hi
>>> obj.a
10
>>> obj.b
20
>>> obj.display()
hi students welcome to django session
>>> 
>>> class Math:
	def add(n1,n2):
		return n1+n2
	def mul(n1,n2):
		return n1*n2

	
>>> class Math:
	def add(n1,n2):
		return n1+n2
	def mul(n1,n2):
		return n1*n2

	
>>> 
>>> m=Math
>>> m.add(6,7)
13
>>> m.mul(8,9)
72
>>> m=Math()
>>> m.add(6,8)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    m.add(6,8)
TypeError: add() takes 2 positional arguments but 3 were given
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class Cons:
	def __init__(self):
		print("myTrail")

		
>>> obj=Cons()
myTrail
>>> class Cons:
	def __init__(self):
		self.a="welcome"
	def show(self):
		print(self.a)

		
>>> obj=Cons()
>>> obj.show()
welcome
>>> class Cons:
	def __myCons__(self):
		print("hi good evening to all")

		
>>> ob=Cons()
>>> ob.__myCons__()
hi good evening to all
>>> class Math:
	def __init__(abc,v1,v2):
		abc.num1=v1
		abc.num2=v2

		
>>> class Math:
	def __init__(abc,v1,v2):
		abc.num1=v1
		abc.num2=v2
	def show(abc):
		print(abc.num1)
		print(abc.num2)
	def add(abc):
		return abc.num1+abc.num2

	
>>> m=Math()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    m=Math()
TypeError: __init__() missing 2 required positional arguments: 'v1' and 'v2'
>>> m=Math(4,5)
>>> m.show()
4
5
>>> m.add()
9
>>> 
