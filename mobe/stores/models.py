from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=100)
    type = models.TextField()
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")

class Category(models.Model):
    name = models.CharField(max_length=20)