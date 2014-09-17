from django.conf.urls import patterns, url

from mixtape.apps.internal_auth.views import (SoundCloudLogin,
                                              SoundCloudGetUrl, HomePage)

urlpatterns = patterns('',
    url(r'^login/', SoundCloudLogin.as_view(),
        name='soundcloud_login'),
    url(r'^redirect/', HomePage.as_view(),
        name='soundcloud_redirect'),

)
