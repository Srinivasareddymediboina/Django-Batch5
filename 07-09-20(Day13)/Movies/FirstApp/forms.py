from django.forms import ModelForm
from FirstApp.models import Movie

class MovieForm(ModelForm):
	class Meta:
		model=Movie
		fields='__all__'

