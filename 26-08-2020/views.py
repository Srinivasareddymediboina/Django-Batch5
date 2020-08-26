from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hi(request):
	return HttpResponse("<h2>hi welcome to django <br> session</h2>")