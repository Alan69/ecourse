from django import forms
from django.forms import ModelForm
from matplotlib import widgets
from .models import Post, TeacherCourse

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

class MyForm2(ModelForm):
  class Meta:
    model = TeacherCourse
    fields = ('topic', 'author', 'author_info', 'about_topic')
    widgets = {
        'topic': forms.TextInput(attrs={'class':'form-control'}),
        'author': forms.TextInput(attrs={'class':'form-control'}),
        'author_info': forms.TextInput(attrs={'class':'form-control'}),
        'about_topic': forms.Textarea(attrs={'class':'form-control'}),
    }