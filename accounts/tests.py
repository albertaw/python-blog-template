from django.test import TestCase
import forms
from django.contrib.auth.models import User

class LoginFormTest(TestCase):
    def test_should_return_user_if_username_and_password_valid(self):
        User.objects.create_user('alberta', password='hello')
        form = forms.LoginForm({'username': 'alberta', 'password': 'hello'})
        form.is_valid()

        self.assertEqual(form.cleaned_data.keys(), ['user'])
        self.assertEqual(form.cleaned_data['user'].username, 'alberta')

    def test_should_make_invalid_form_if_blank_username(self):
        form = forms.LoginForm({'username': '', 'password':'hello'})
        self.assertFalse(form.is_valid())

    def test_should_make_invalid_form_if_blank_password(self):
        form = forms.LoginForm({'username': 'alberta', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_should_make_form_invalid_if_username_and_password_do_not_match(self):
        form = forms.LoginForm({'username': 'ally', 'password': 'hi'})
        self.assertFalse(form.is_valid())
