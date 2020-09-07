from django.db import models

# Create your models here.
class Library(models.Model):
	branches = (
		('ece','ECE'),
		('cse','CSE'),
		('it','IT'),
		('mech','MECH'),
		('civil','CIVIL'),
		('chem','CHEM')
	)
	
	Book_Number = models.IntegerField()
	Book_Name = models.CharField(max_length=50)
	Book_Author = models.CharField(max_length=30)
	Department = models.CharField(max_length=10,choices=branches)
	Publication_Date = models.DateField()
