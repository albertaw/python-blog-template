from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows': 5}))