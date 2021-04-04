from django import forms
from django.core import validators


def z_name(value):
    print(f'VALUE: {value}')
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name must start with z')


class FormName(forms.Form):
    name = forms.CharField(validators=[z_name])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])
