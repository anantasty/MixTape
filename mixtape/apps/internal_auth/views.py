from django.views.generic.base import View
from django import http
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from mixtape.apps.internal_auth.forms import SoundCloudLoginForm
from mixtape.apps.internal_auth import soundcloud_utils


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

    def get(self, request):
        print "out_req session_id = {}".format(request.session.session_key)
        return http.HttpResponseRedirect(soundcloud_utils.get_login_url(
            request))


class HomePage(View):
    template_name = 'home_page.html'

    def get(self, request):
        return render(request, self.template_name)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse(login_redirect(request.user)))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active is not False:
                if not request.POST.get('remember'):
                    request.session.set_expiry(0)
                auth.login(request, user)
                return HttpResponseRedirect(settings.LOGIN_ERROR_URL)
        else:
            return HttpResponseRedirect(settings.LOGIN_ERROR_URL)
    else:
        render(request, 'login.html', {})

    return render(request, 'login.html', {})
