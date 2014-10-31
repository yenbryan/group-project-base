from django.core.exceptions import ValidationError
from django.test import TestCase
from slides.forms import ProfileForm
from slides.models import Profile


class FormTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create_user(username='test-user')

    def test_clean_username_exception(self):
        # set up the form for testing
        form = ProfileForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username(self):
        # set up the form for testing
        form = ProfileForm()
        form.cleaned_data = {'username': 'test-user2'}

        self.assertEqual(form.clean_username(), 'test-user2')

    def test_save_user(self):
        # test save def in ProfileForm
        user_info = {
            'username': 'test-user3',
            'password1': 'test',
            'password2': 'test',
            'real_name': 'test test',
            'email': 'email@email.com',
        }
        form = ProfileForm(user_info)
        self.assertEqual(form.save().username, user_info['username'])
