from django.db import models

# Create your models here.

class Student(models.Model):
	First_Name = models.CharField(max_length=30)
	Last_Name = models.CharField(max_length=30)
	Branch = models.CharField(max_length=10)
	Age = models.IntegerField()
	Email = models.EmailField()

	def __str__(self):
		return self.First_Name+' '+self.Last_Name