from django.forms import ModelForm
from .models import Library

class LibraryForm(ModelForm):
	class Meta:
		model = Library
		fields = '__all__' # all the models fields
		# fields = ['Book_Name','Book_Author'] # specific fields
