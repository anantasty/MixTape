from django import forms


class SoundCloudLoginForm(forms.Form):
    token = forms.CharField(label='soundcloud token', max_length=100)
