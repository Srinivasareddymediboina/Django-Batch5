from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'home.html')

def register(request):
	if request.method=='POST':
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		female = request.POST.get('f')
		male = request.POST.get('m')
		if female=='on':
			gender = 'Female'
		elif male == 'on':
			gender = 'Male'
		branch = request.POST.get('br')
		mail = request.POST.get('mail')

		data = {'fname':fname,'lname':lname,'gender':gender,'branch':branch,'mail':mail}

		return render(request,'data.html',data)
		
	return render(request,'register.html')
