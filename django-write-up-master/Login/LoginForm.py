import django.forms


class LoginForm(django.forms.Form):
    email = django.forms.EmailField(widget=django.forms.EmailInput(attrs={'style' : 'display: block;','class' : 'form'}))
    password = django.forms.CharField(widget=django.forms.PasswordInput(attrs={'style' : 'display: block;','class' : 'form'}))