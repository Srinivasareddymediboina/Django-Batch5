from django.shortcuts import render
from EmailSend import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
import random
from FirstApp.models import EmailUser
# Create your views here.
def mail(request):
	if request.method=='POST':
		tomail=request.POST['email']
		sub=request.POST['sub']
		msg=request.POST['msg']
		sender=settings.EMAIL_HOST_USER
		receiver=tomail
		email=EmailMessage(sub,msg,sender,[receiver])
		email.content_subtype='html'
		file=request.FILES['file']
		email.attach(file.name,file.read(),file.content_type)
		email.send()
		return HttpResponse('Email Send Successfully')

	return render(request,'mail.html')

def register(request):
	if request.method=='POST':
		fname=request.POST['fname']
		lname=request.POST['lname']
		username=request.POST['username']
		email=request.POST['email']
		dob=request.POST['dob']
		pwd=str(random.randint(100000,999999))
		try:
			EmailUser.objects.create(fname=fname,lname=lname,username=username,
			email=email,dob=dob,password=pwd)
		except:
			return HttpResponse("This User is Already Exist")

		Sub="Reg to your Login Details"
		body="""Hello {}\n\n This is your Username: {}\n\n\n your password: {}\n\n""".format(username,username,pwd)

		sender=settings.EMAIL_HOST_USER
		receiver=email
		email=EmailMessage(Sub,body,sender,[receiver])
		email.send()
		return HttpResponse('Please check your mail for login details')

	return render(request,'register.html')

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		pwd=request.POST['password']
		data=EmailUser.objects.all().filter(username=username,password=pwd)
		if data:
			return render(request,'welcome.html',{'user':username})
		else:
			return HttpResponse('Invalid User')

	return render(request,'login.html')

def forgetpwd(request):
	if request.method=='POST':
		email=request.POST['email']
		data=EmailUser.objects.get(email=email)
		sub="reg your password..."
		body="Your Username: "+data.username+"\n\n Your Password: "+data.password
		sender=settings.EMAIL_HOST_USER
		receiver=email
		e=EmailMessage(sub,body,sender,[receiver])
		e.send()
		return HttpResponse('Check your Mail for Password')
	return render(request,'forgetpwd.html')

def changepwd(request):
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		data=EmailUser.objects.get(password=oldpass)
		if newpass != conpass:
			return HttpResponse("Password Does't match")
		else:
			data.password=conpass
			data.save()
			return HttpResponse("Your Password is updated")
			
	return render(request,'changepwd.html')