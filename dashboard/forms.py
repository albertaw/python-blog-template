from django import forms


class DashboardForm(forms.Form):
    # use form widgets to customize the fields
    # https://docs.djangoproject.com/en/1.10/ref/forms/widgets/
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=False)
    email = forms.CharField(required=False)
