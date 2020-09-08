from django.db import models

# Create your models here.
class Movie(models.Model):
	moviename=models.CharField(max_length=50)
	heroname=models.CharField(max_length=50)
	heroinname=models.CharField(max_length=50)
	poster=models.ImageField(upload_to='poster/',null=True)
	director=models.CharField(max_length=50)
	reldate=models.DateField(null=True)
