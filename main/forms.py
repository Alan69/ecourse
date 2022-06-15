from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import Post

class MyForm(ModelForm):
  class Meta:
    model = Post
    fields = ('name', 'email', 'subject', 'message')
    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'email': forms.TextInput(attrs={'class':'form-control'}),
        'subject': forms.TextInput(attrs={'class':'form-control'}),
        'message': forms.Textarea(attrs={'class':'form-control'}),
    }