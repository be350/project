from django.db import models

# Create your models here.
class Login(models.Model):
    Uid= models.CharField(max_length = 20)
    PWD = models.CharField(max_length = 20)