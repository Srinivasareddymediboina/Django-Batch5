from django.urls import path
from . import views # from student import views



urlpatterns = [
	path('home/',views.home,name='home'),
	path('register/',views.register,name='register'),
	path('show/',views.show,name='show')
]