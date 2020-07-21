from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharFiield(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    password = forms.CharFiield(widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharFiield(widget=forms.TextInput(attrs={ 'class': 'form-control'}))
    email = forms.CharFiield(widget=forms.EmailInput(attrs={ 'class': 'form-control'}))
    password = forms.CharFiield(label= 'Password',widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))
    confirm_password = forms.CharFiield(label= 'Confirm password',widget=forms.PasswordInput(attrs={ 'class': 'form-control'}))
    

        