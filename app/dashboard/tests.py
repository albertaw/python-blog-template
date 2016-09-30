from django.test import TestCase
from django.contrib.auth.models import User
import forms


class Dashboard(TestCase):

    def test_should_make_form_valid_for_username(self):
        form = forms.DashboardForm({'username':'test', 'email': 'test@example.com'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['username'], 'test')

    def test_should_make_form_valid_for_email(self):
        form = forms.DashboardForm({'username': 'test', 'email': 'test@example.com'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['email'], 'test@example.com')

    def test_should_make_form_valid_form_blank_username(self):
        form = forms.DashboardForm({'username': '', 'email': 'test@example.com'})
        self.assertTrue(form.is_valid())

    def test_should_make_form_valid_for_blank_email(self):
        form = forms.DashboardForm({'username': 'test', 'email': ''})
        self.assertTrue(form.is_valid())

    def test_should_make_form_invalid_for_username_that_already_exists(self):
        user = User.objects.create_user(username='test', email='test@example.com')
        form = forms.DashboardForm({'username': 'test', 'email': 'test@example.com'})
        self.assertFalse(form.is_valid())