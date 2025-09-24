import email
import django.forms

class Input(django.forms.Form):
    email = django.forms.CharField()
    textarea = django.forms.CharField(widget=django.forms.Textarea(attrs={'rows':'4','cols':'50'}))
    privacy = django.forms.CharField(widget=django.forms.CheckboxInput(attrs={'value' : 'False'}),required=False)

class Email(django.forms.Form):
    email = django.forms.CharField()
    
class ImageForm(django.forms.Form):
    email = django.forms.CharField()
    img = django.forms.ImageField()