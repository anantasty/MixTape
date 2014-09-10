from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixtape.views.home', name='home'),
                       url(r'^auth/', include('mixtape.apps.auth.urls',
                                              namespace='auth')),

    url(r'^admin/', include(admin.site.urls)),
)
