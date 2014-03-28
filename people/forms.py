from django import forms

class JoinForm(forms.Form):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    university = forms.CharField()
    degree_subject = forms.CharField()
    graduation_year = forms.IntegerField()