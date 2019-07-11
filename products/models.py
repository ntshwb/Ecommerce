from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2048)
    description = models.CharField(max_length=255)
    location = models.CharField(default='', max_length=255)
