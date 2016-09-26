from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PostForm(forms.Form):
    # use form widgets to customize the fields
    # https://docs.djangoproject.com/en/1.10/ref/forms/widgets/
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    content = forms.CharField(widget=forms.Textarea())