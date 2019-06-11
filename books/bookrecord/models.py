from django.db import models

# Create your models here.
class bookrecord(models.Model):
	bname=models.CharField(max_length=200)
	bauthor=models.CharField(max_length=200)
	bquantity=models.CharField(max_length=100)



