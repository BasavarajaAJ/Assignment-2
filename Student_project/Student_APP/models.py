from django.db import models

class Intrest(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,default="") 
    USN= models.CharField(max_length=3,default="")
    clg_name= models.CharField(max_length=15,default="")
    intrests=models.ManyToManyField(Intrest)

    def __str__(self):
        return self.name

