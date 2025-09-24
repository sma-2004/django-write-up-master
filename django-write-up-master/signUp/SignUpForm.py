import django.forms


class SignUpForm(django.forms.Form):
    First_Name = django.forms.CharField(widget=django.forms.TextInput(attrs={'style' : 'display: block;','class' : 'form'}))
    Last_Name = django.forms.CharField(widget=django.forms.TextInput(attrs={'style' : 'display: block;','class' : 'form'}))
    email = django.forms.EmailField(widget=django.forms.EmailInput(attrs={'style' : 'display: block;','class' : 'form'}),required=False)
    New_password = django.forms.CharField(widget=django.forms.PasswordInput(attrs={'style' : 'display: block;','class' : 'form'}))
    Confirm_password = django.forms.CharField(widget=django.forms.PasswordInput(attrs={'style' : 'display: block;','class' : 'form'}))
    OTP = django.forms.CharField(required=False)