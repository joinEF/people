from django import forms
from django.contrib.auth.models import User

from models import UserProfile, Project

class JoinForm(forms.Form):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    university = forms.CharField()
    degree_subject = forms.CharField()
    graduation_year = forms.IntegerField()

class AccountForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    university = forms.CharField()
    degree_subject = forms.CharField()
    graduation_year = forms.IntegerField()

    location = forms.CharField()
    twitter = forms.CharField()
    github = forms.CharField()
    linkedin = forms.CharField()
    url = forms.URLField()
    description = forms.CharField(widget=forms.Textarea)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('user',)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project