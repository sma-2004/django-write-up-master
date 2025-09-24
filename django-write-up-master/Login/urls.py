from django.urls import path
from Login.views import *

urlpatterns = [
    path('',logIn,name="login"),
]