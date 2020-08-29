from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
	return render(request,'firstApp/sample.html')
def signup(request):
	if request.method=="POST":
		name=request.POST['uname']
		mobile=request.POST['mbno']
		Email=request.POST['email']
		return HttpResponse("added successfully")
	return render(request,'firstApp/signup.html')