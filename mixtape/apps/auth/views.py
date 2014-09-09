from django.views.generic.base import View
from django import http
from mixtape.apps.auth.forms import SoundCloudLoginForm
from mixtape.apps.auth import soundcloud_utils


class SoundCloudLogin(View):
    form_class = SoundCloudLoginForm

    def get(self, request):
        form = SoundCloudLoginForm(request)
        code = form.fields['code']
        print code
        return http.JsonResponse({'code': code})


class SoundCloudGetUrl(View):

    def get(self, requeest):
        return http.HttpResponseRedirect(soundcloud_utils.get_login_url())



