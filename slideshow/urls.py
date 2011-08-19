from django.conf.urls.defaults import *



urlpatterns = patterns('slideshow.views',
    
    (r'^show/(?P<slideshow_slug>[-\w]+)/$', 'view_slideshow', {}, 'view_slideshow'),

    (r'^(?P<slideshow_slug>[-\w]+)/settings.xml$', 'slideshow_settings', {}, 'slideshow_settings'),

)
