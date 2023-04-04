from django.db import models

# Create your models here.

class employee(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),('O', 'Other'),]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date =models.DateField()
    department =models.CharField(max_length=50)
