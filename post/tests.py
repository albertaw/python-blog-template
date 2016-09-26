from django.test import TestCase
import forms
# Create your tests here.

class Post(TestCase):

    def test_should_make_form_valid_if_content(self):
        form = forms.PostForm({'title': 'test','content':'This is a test'})
        self.assertTrue(form.is_valid())

    def test_should_make_form_invalid_if_no_content(self):
        form = forms.PostForm({'content':''})
        self.assertFalse(form.is_valid())

    def test_should_make_form_invalid_if_no_title(self):
        form = forms.PostForm({'title': '','content':'hello world'})
        self.assertFalse(form.is_valid())