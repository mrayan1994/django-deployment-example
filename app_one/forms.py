from django import forms
# from django.core import validators
from django.contrib.auth.models import User
from app_one.models import UserProfileInfo


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoFrom(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('portfolio', 'picture')


# def check_name_for_z(value):
#
#     if value[0].lower() != 'z':
#
#         raise forms.ValidationError("Name needs to start with z")
#
#
# class TestForm(forms.Form):
#
#     name = forms.CharField(validators=[check_name_for_z])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your Email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
#
#     def clean(self):
#
#         all_clean_data = super().clean()
#         email = all_clean_data.get('email')
#         vemail = all_clean_data.get('verify_email')
#
#         if email != vemail:
#             raise forms.ValidationError("Emails don't match")
#
#     def clean_botcatcher(self):
#
#         botcatcher = self.cleaned_data.get('botcatcher')
#         if len(botcatcher) > 0:
#             raise forms.ValidationError("BOT Detected")
#         return botcatcher
