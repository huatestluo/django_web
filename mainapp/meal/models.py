from django.db import models

# Create your models here.

class Confinement(models.Model):
    name = models.CharField(max_length=20)
    practice = models.CharField(max_length=500)

class Tsukiko(models.Model):
    name = models.CharField(max_length=20)
    practice = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)