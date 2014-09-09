from django.conf.urls import patterns, url

from mixtape.apps.auth.views import SoundCloudLogin, SoundCloudGetUrl

urlpatterns = patterns('',
    url(r'^login/', SoundCloudLogin.as_view(),
        name='soundcloud_login'),
    url(r'^redirect/', SoundCloudGetUrl.as_view(),
        name='soundcloud_redirect'),

)
