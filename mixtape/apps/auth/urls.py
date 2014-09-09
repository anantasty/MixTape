from django.conf.urls import patterns, url

from mixtape.apps.auth.views import SoundCloudLogin

urlpatterns = patterns('',
    url(r'^login/', SoundCloudLogin.as_view(),
        name='soundcloud_login'),
)
