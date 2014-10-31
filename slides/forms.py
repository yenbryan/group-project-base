import email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.forms import ModelForm
from slides.models import Profile
from django.utils.translation import ugettext, ugettext_lazy as _


class ProfileForm(UserCreationForm):
    helper = FormHelper()
    helper.form_method = "POST"
    helper.form_class = "form-horizontal"
    helper.add_input(Submit('Register', 'Register', css_class='btn-default'))

    real_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ("username", "password1", "password2", "real_name", "email",  "image")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            self._meta.model._default_manager.get(username=username)
        except self._meta.model.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(ProfileForm, self).save(commit=commit)
        # text_content = 'Thank you for signing up for our website at {}, {} {}'\
        #     .format(user.date_joined, user.first_name, user.last_name)
        # html_content = '<h2>Thanks {} {} for signing up at {}!</h2> <div>I hope you enjoy using our site</div>'\
        #     .format(user.first_name, user.last_name, user.date_joined)
        # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()
        return user


class UpdateUserImageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ("image",)
