from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    standard = models.IntegerField()
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)

