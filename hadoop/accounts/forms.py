# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import StrictButton


# class UserProfileForm(forms.ModelForm):
#     #按照这个模式来设定样式
#     true_name = forms.CharField(max_length=20, required=False)
#     gender = forms.ChoiceField(required=False, choices=GENDER)
#     college = forms.CharField(max_length=40, required=False,
#                               widget=forms.TextInput(attrs={'placeholder': '学校', 'class': 'input-xlarge'}))
#     birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'input-xlarge'}))
#     phone = forms.CharField(max_length=11, required=False)
#     qq = forms.CharField(max_length=11, required=False)
#     description = forms.CharField(max_length=140, required=False, widget=forms.Textarea)

#     class Meta:
#         model = UserProfile
#         exclude = ['user',]

# user = User.objects.create_user('czl', '112358')
# user.save()

class SignInForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    password = forms.CharField(max_length=128)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-signin'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Fieldset(
                'please sign in',
                'name',
                'password',
                )
            )

    class Meta:
        model = User


# class OrganizationForm(forms.ModelForm):

#     name = forms.CharField(max_length = 256)
#     official_link = forms.CharField(max_length = 1024)

#     def __init__(self, *args, **kwargs):
#         super(OrganizationForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_class = 'form-horizontal'
#         self.helper.label_class = 'col-sm-2'
#         self.helper.field_class = 'col-sm-4'
#         self.helper.layout = Layout(
#             Fieldset(
#                 'Join Volunteer Organization',
#                 'name',
#                 'official_link',
#                 StrictButton('Sign Up', value='Create', css_class='btn btn-default col-sm-offset-2'),
#             ),
#         )

#     class Meta:
#         model = Organization
#         exclude = ('memebers', )
