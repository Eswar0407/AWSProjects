from django.db import models

# Create your models here.
class productinfoModel(models.Model):
    number = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    photo = models.ImageField()