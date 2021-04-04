from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    email_confirmation = forms.EmailField(label='Confirm email')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        clean_data = super().clean()
        email = clean_data['email']
        conf = clean_data['email_confirmation']

        if email != conf:
            raise forms.ValidationError('Email confirmation does not match email')
