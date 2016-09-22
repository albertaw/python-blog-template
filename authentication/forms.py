from django import forms

# need deeper understanding-I'm inheriting from forms.Form?
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()