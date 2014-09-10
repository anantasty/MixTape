from django.views.generic.base import View
from django import http
from mixtape.apps.auth.forms import SoundCloudLoginForm
from mixtape.apps.auth import soundcloud_utils


class SoundCloudLogin(View):
    form_class = SoundCloudLoginForm

    def get(self, request):
        print "in req session_id = {}".format(request.session.session_key)
        form = SoundCloudLoginForm(request.GET)
        if form.is_valid():
            code = form.cleaned_data['code']
            return http.JsonResponse({'code': code})
        return http.JsonResponse({'code': 'FAILED'})


class SoundCloudGetUrl(View):

    def get(self, requeest):
        print "out_req session_id = {}".format(request.session.session_key)
        return http.HttpResponseRedirect(soundcloud_utils.get_login_url())



