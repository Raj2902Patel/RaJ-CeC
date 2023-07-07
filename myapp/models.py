from django.db import models

# Create your models here.

class raj(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
