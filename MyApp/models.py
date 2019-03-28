from django.db import models
from django.utils import timezone

# Create your models here.

class Emp(models.Model):
	eid=models.CharField(max_length=4)
	ename=models.CharField(max_length=20)
	dob=models.DateTimeField(default=timezone.now())
	email=models.EmailField(max_length=50,verbose_name='E-Mail',default='example@gmail.com')
	
	def __str__(self):
		return self.ename
