from django.db import models

# Create your models here.

class Faculty(models.Model):
	branches = (
		('ece','ECE'),
		('cse','CSE'),
		('it','IT'),
		('me','Mech'),
		('ce','Civil')
		)
	Name = models.CharField(max_length=30)
	Qualification = models.CharField(max_length=20,blank=True,null=True)
	Department = models.CharField(max_length=10,choices=branches)
	Email = models.EmailField(default='example@gmail.com')
	Phone = models.CharField(max_length=10,help_text='Enter 10 Digit Mobile Number')

	def __str__(self):
		return self.Name

	class Meta:
		verbose_name_plural = 'Faculty'
		db_table = 'College'