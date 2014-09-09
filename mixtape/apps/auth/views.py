from django.views.generic.base import View
from django import http
from mixtape.apps.auth.forms import SoundCloudLoginForm


class SoundCloudLogin(View):
    form_class = SoundCloudLoginForm

    def post(self, request):
        form = SoundCloudLoginForm(request)
        print form.token


