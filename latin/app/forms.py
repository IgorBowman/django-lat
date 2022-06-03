from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Country
from captcha.fields import CaptchaField


class CountryForm(ModelForm):
    captcha = CaptchaField()
    description = forms.Textarea(attrs={'colors': 40, 'rows': 10})

    class Meta:
        model = Country
        exclude = ('images',)
        labels = {"name": 'Название страны'}


class RegisterUserForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
