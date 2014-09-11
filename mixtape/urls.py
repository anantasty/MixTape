from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixtape.views.home', name='home'),
                       url(r'^auth/', include('mixtape.apps.internal_auth.urls',
                                              namespace='auth')),
                       url(r'^login/$',
                           'django.contrib.auth.views.login',
                           name='login'),
    #socialauth url
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
