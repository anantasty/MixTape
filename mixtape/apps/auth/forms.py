from django import forms


class SoundCloudLoginForm(forms.Form):
    code = forms.CharField(label='soundcloud token', max_length=100)
