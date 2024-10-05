from django import forms
from .models import Video,Comment

class VideoForm(forms.ModelForm):
  class Meta:
      model=Video
      fields=['link','title','category']
      widgets = {
            'link': forms.URLInput(attrs={'placeholder': 'Enter Youtube Address','class': 'form_input'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter youtube Title','class': 'form_input'}),
            'category': forms.Select(attrs={'placeholder': 'Selcet a a Category For the video','class': 'form_input choice_input'}),
        }
      
class CommentForm(forms.ModelForm):
  class Meta:
    model=Comment
    fields=['comment_text']
    widgets={
    'comment_text':forms.TextInput(attrs={'placeholder': 'Add a comment','class': 'form_input',})
    }
    labels = {
            'comment_text': '',  # This removes the label
        }