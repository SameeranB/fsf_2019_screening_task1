from django import forms

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder' : 'Username'}), label='')
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password'}), label='')

