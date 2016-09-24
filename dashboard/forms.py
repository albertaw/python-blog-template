from django import forms
from django.contrib.auth.models import User


class DashboardForm(forms.Form):
    # use form widgets to customize the fields
    # https://docs.djangoproject.com/en/1.10/ref/forms/widgets/
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # make fields false to avoid returning errors with empty fields
    username = forms.CharField(required=False, )
    email = forms.CharField(required=False)

    # override the form to accept a second argument-the current logged in user
    # def __init__(self, *args, **kwargs):
    #    self.user = kwargs.pop('user')
    #    super(DashboardForm, self).__init__(*args, **kwargs)

    def validate_username(self, user):
        old_username = user.username
        print old_username

        new_username = self.cleaned_data['username']
        print new_username
        if old_username == new_username:
            return old_username
        else:
            # if the changed username is not the same check if it exists for another user
            try:
                User.objects.get(username=new_username)
            except User.DoesNotExist:
                return new_username
            finally:
                return old_username





