from django.shortcuts import render,redirect
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

def edit(request,id):
	data = Student.objects.get(id=id)
	if request.method=='POST':
		data.First_Name = request.POST.get('fname')
		data.Last_Name = request.POST.get('lname')
		data.Age = request.POST.get('age')
		data.Branch = request.POST.get('br')
		data.Email = request.POST.get('mail')
		data.save()
		return redirect('show')
	return render(request,'student/edit.html',{'data':data})

def delete(request,id):
	data = Student.objects.get(id=id)
	return render(request,'student/delete.html',{'data':data})

def confirm(request,id):
	data = Student.objects.get(id=id)
	data.delete()
	return redirect('show')