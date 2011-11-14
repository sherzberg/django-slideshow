from django.conf.urls.defaults import patterns



urlpatterns = patterns('slideshow.views',
    
    (r'^show/(?P<slideshow_slug>[-\w]+)/$', 'view_slideshow', {}, 'view_slideshow'),

    (r'^(?P<slideshow_slug>[-\w]+)/settings.xml$', 'slideshow_settings', {}, 'slideshow_settings'),

    (r'^bulkupload/$', 'slideshowimage_bulk_upload', {}, 'slideshowbulkupload'),
)
