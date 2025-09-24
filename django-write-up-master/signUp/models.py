from django.db import models
from django.forms import ModelForm
# Create your models here.
class User(models.Model):
    FullName = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

# class SignUpForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['FullName','email','password']