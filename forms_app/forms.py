from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean_bot_catcher(self):
        bot_catcher = self.cleaned_data['bot_catcher']
        if len(bot_catcher) > 0:
            raise forms.ValidationError('Nice try, bot')
