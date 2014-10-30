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


# class UpdatePasswordForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ("password",)


# class UpdateProfileForm(forms.ModelForm):
#     real_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = Profile
#         fields = ("image", "real_name", "email", "password1", "password2")
#
#
#     def save(self, commit=True):
#         user = super(UpdateProfileForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#
#         if commit:
#             user.save()
#
#         return user

# class UserEditForm(forms.Form):
#     image = forms.ImageField(label="profile picture")
#     real_name = forms.CharField(label="your real name", required=True)
#     email = forms.EmailField(label="email")
#     password1 = forms.CharField(label="password1", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="password2", widget=forms.PasswordInput)
#     # think about password input

# class UserChangeForm(forms.ModelForm):
#     real_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     # username = forms.RegexField(
#     #     label=_("Username"), max_length=30, regex=r"^[\w.@+-]+$",
#     #     help_text=_("Required. 30 characters or fewer. Letters, digits and "
#     #                 "@/./+/-/_ only."),
#     #     error_messages={
#     #         'invalid': _("This value may contain only letters, numbers and "
#     #                      "@/./+/-/_ characters.")})
#     password = ReadOnlyPasswordHashField(label=_("Password"),
#         help_text=_("Raw passwords are not stored, so there is no way to see "
#                     "this user's password, but you can change the password "
#                     "using <a href=\"password/\">this form</a>."))
#
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(UserChangeForm, self).__init__(*args, **kwargs)
#         f = self.fields.get('user_permissions', None)
#         if f is not None:
#             f.queryset = f.queryset.select_related('content_type')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]