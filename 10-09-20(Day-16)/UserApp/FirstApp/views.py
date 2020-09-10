from django.shortcuts import render
from FirstApp.forms import MyForm
from django.http import HttpResponse
# Create your views here.
def home(request):

	return render(request,'home.html')
	
def register(request):
	if request.method=='POST':
		data=MyForm(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse('User Registered Successfully')
		else:
			return HttpResponse("Please enter Valid data")
			
	form=MyForm()
	return render(request,'register.html',{'form':form})