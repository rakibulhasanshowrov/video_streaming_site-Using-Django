from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class loginForm(AuthenticationForm):
  username = forms.CharField(
        required=True,
        label='Username:',
        widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form_input'})
    )
  password = forms.CharField(
        required=True,
        label='Password:',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form_input'})
    )