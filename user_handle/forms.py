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
  class Meta:
      model = User
      fields=['username','password']
  
class signupForm(UserCreationForm):
  email=forms.EmailField(required=True,label='Email:',widget=forms.TextInput(attrs={'placeholder':"Email",'class': 'form_input'}))
  username=forms.CharField(required=True,label='Username:',widget=forms.TextInput(attrs={'placeholder':"Username",'class': 'form_input'}))
  password1=forms.CharField(required=True,label='Password:',widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form_input'}))
  password2=forms.CharField(required=True,label='Confirm Password:',widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation','class': 'form_input'}))
  class Meta:
      model = User
      fields=['username','email','password1','password2',]

class UserProfileForm(forms.ModelForm):
  class Meta:
    model=UserProfile
    fields='__all__'
    exclude=['user']
    widgets={
      'dob':forms.DateInput(attrs={'type': 'date','class':'date_input'}),
      'profile_pic':forms.FileInput(attrs={'class':'file_input',}),
      'profile_type':forms.Select(attrs={'class':'choice_input',})
    }
    labels = {
            'dob': 'Date Of Birth',  # This removes the label
        }
    