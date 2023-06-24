from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import CustomUser


class TraderCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        error_messages = {
            'username': {
                'unique': 'A user with that username already exists.',
                'required': 'Please enter a valid username.',
            },
            'password2': {
                'required': 'Please confirm your password.',
            }
        }


class TraderLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

