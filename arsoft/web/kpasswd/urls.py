from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'arsoft.web.kpasswd.views.home', name='home'),
    url(r'^changepw$', 'arsoft.web.kpasswd.views.changepw', name='changepw'),
#    url(r'^%s$' % settings.BASE_URL, 'arsoft.web.kpasswd.views.home', name='home'),
#    url(r'^%s/changepw$' % settings.BASE_URL, 'arsoft.web.kpasswd.views.changepw', name='changepw'),
    # url(r'^arsoft.web.kpasswd/', include('arsoft.web.kpasswd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from arsoft.web.utils import django_debug_urls
django_debug_urls(__name__, __file__)
