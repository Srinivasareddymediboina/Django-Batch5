from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'student/home.html')

def register(request):
	if request.method=='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		age = request.POST.get('age')
		branch = request.POST.get('br')
		mail = request.POST.get('mail')

		# data = {'fname':fname,'lname':lname,'gender':gender,'branch':branch,'mail':mail}
		obj = Student(First_Name=fname,Last_Name=lname,Branch=branch,Age=age,Email=mail)
		obj.save()
		return HttpResponse("Registration Successful !")
		
	return render(request,'student/register.html')


def show(request):
	data = Student.objects.all()
	return render(request,'student/data.html',{'data':data})