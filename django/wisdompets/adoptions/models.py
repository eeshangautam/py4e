from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('F','Female')] #constant name is defined
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
