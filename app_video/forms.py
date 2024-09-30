from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
  class Meta:
      model=Video
      fields=['link','title','category']
      widgets = {
            'link': forms.URLInput(attrs={'placeholder': 'Enter Youtube Address','class': 'form_input'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter youtube Title','class': 'form_input'}),
            'category': forms.Select(attrs={'placeholder': 'Selcet a a Category For the video','class': 'form_input'}),
        }