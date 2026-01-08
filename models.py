from django.db import models

# Create your models here.
class bloodbank(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    num=models.BigIntegerField()
    note=models.CharField(max_length=100)
