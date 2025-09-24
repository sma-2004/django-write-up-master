from distutils.command.upload import upload
import email
from email.policy import default
from operator import mod
from django.db import models

class text(models.Model):
    id = models.CharField(primary_key=True,max_length=500)
    email = models.CharField(max_length=100)
    text = models.CharField(max_length=(9999999999999999999999999999999999*9999999999999999999999999999999999999999999))
    privacy = models.BooleanField(default=False)
    likes = models.CharField(max_length=100,default="")
    likesCount = models.IntegerField(default=0)
    
# class temptext(models.Model):
#     txt = models.CharField(max_length=(9999999999999999999999999999999999*9999999999999999999999999999999999999999999))

class Img(models.Model):
    email = models.CharField(primary_key=True,max_length=100)
    img = models.ImageField(default="",upload_to = 'profiles/Imgs')