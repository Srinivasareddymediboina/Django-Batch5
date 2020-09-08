from django.shortcuts import render
from myApp.forms import LibraryForm
from django.http import HttpResponse
from django.contrib import messages
from myApp.models import Library
# Create your views here.
def register(request):
	form=LibraryForm(request.POST,request.FILES)
	if form.is_valid():
		form.save()
		#return HttpResponse('Done')
		messages.warning(request,request.POST['Book_Name']+' is Succefully Registered')

	form=LibraryForm()
	return render(request,'register.html',{'form':form})

def show(request):
	data=Library.objects.all()
	return render(request,'show.html',{'data':data})
