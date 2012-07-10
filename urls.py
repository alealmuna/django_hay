from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin 

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_hay.views.home', name='home'),
    # url(r'^django_hay/', include('django_hay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    (r'^search/', include('haystack.urls')),
)
