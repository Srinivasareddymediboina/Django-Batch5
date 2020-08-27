from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	name="srikanya"
	return HttpResponse("hi"+name+"welcome to django session")
def index(request,name):
	return HttpResponse("<h1>hi my name is :</h1>"+name)
def sg(request,name,id):
	return HttpResponse("your name is :{} <br> your id is :{}".format(name,id))
def message(request):
	return render(request,'myApp/message.html',{})
def details(request):
	data={'name':'sri','rollno':659}
	return render(request,'myApp/details.html',{'data':data})
def register(request):
	if request.method=="POST":
		name=request.POST['uname']
		mobile=request.POST['mbno']
		email=request.POST['email']
		print(name,mobile,email)
		return HttpResponse("your record is added successfully")
	return render(request,'myApp/register.html',{})