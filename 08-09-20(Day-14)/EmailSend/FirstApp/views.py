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
		EmailUser.objects.create(fname=fname,lname=lname,username=username,
			email=email,dob=dob,password=pwd)
		Sub="Reg to your Login Details"
		body="""Hello {}\n\n This is your Username: {}\n\n\n your password: {}\n\n""".format(username,username,pwd)

		sender=settings.EMAIL_HOST_USER
		receiver=email
		email=EmailMessage(Sub,body,sender,[receiver])
		email.send()
		return HttpResponse('Please check your mail for login details')

	return render(request,'register.html')