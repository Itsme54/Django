from django import forms
from .models import *


class CreatepostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'blog_content']


class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    form_body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
