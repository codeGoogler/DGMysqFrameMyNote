from django.db import models

# Create your models here.


class UserInfo(models.Model):
    userName = models.CharField(max_length=10)
    userPassword= models.CharField(max_length=40)
    idDelete = models.BooleanField()