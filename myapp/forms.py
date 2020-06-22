from django import forms
from myapp.models import *

class LoginForm(forms.Form):
    username = forms.EmailField()
    name = forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput())

# class MyForm(forms.ModelForm):
#     class Meta:
#         model=Student
#         fields=['name','age','height']
#
#
#
class UploadForm(forms.Form):
    name=forms.CharField(max_length=250)
    image=forms.ImageField()
