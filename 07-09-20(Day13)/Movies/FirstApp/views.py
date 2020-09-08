from django.shortcuts import render
from FirstApp.forms import MovieForm
from django.http import HttpResponse
from FirstApp.models import Movie
from django.contrib import messages
# Create your views here.
def register(request):
	form=MovieForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		messages.warning(request,'Movie is added successfully')

	form=MovieForm()
	return render(request,'register.html',{'form':form})

def showall(request):
	data=Movie.objects.all()
	return render(request,'showall.html',{'data':data})
