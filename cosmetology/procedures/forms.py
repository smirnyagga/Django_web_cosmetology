from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *
from django.forms import ModelForm, Textarea, NumberInput, TextInput, EmailInput


class ApplicationForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Applications
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'message': Textarea(attrs={'placeholder': 'На какую процедуру Вы бы хотели попасть?',
                                       'class': 'form-input-big'}),
            'phone': NumberInput(attrs={'class': 'form-input'}),
            'email': EmailInput(attrs={'placeholder': 'На всякий случай, если не дозвонимся.',
                                       'class': 'form-input'}),
            'name': TextInput(attrs={'class': 'form-input'})
        }


class QuestionForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Questions
        fields = ['name', 'question']
        widgets = {
            'question': forms.Textarea(attrs={'placeholder': 'Напишите тут ваш вопрос, отзыв, пожелание', 'class': 'form-input-big'}),
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Имя пользователя:')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input'}), label='Email:')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Пароль:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Повтор пароля:')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Имя пользователя:')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}), label='Пароль:')
