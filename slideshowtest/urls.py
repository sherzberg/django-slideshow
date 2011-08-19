from django.conf.urls.defaults import *
from django.conf import settings

import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^slideshow/', include('slideshow.urls')),

    (r'^test/$', 'slideshowtest.views.test'),


    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #statics pages
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : os.getcwd()+'/media'}),
)



