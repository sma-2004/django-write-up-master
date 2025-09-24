from django.urls import path
from signUp.views import *
urlpatterns = [
    path('',SignUp,name="signUp"),
    path('otp',getOtp,name="otp"),
    # path('mail',email,name="mail")
    # path('email',email,name="email")
]