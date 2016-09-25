from django import forms
from django.contrib.auth import authenticate

# need deeper understanding-I'm inheriting from forms.Form?
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if 'username' in cleaned_data and 'password' in cleaned_data:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user == None:
                raise forms.ValidationError('incorrect username/password')
            cleaned_data['user'] = user
            del cleaned_data['username']
            del cleaned_data['password']

        return cleaned_data
