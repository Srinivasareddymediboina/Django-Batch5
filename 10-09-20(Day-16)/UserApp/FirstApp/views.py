from django.shortcuts import render
from FirstApp.forms import MyForm
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
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
	
@login_required
def profile(request,id):
	data=User.objects.get(id=id)
	return render(request,'profile.html',{'data':data})