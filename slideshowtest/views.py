from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.template.loader import get_template

from slideshow.models import Slideshow, SlideshowImage

def test(request, template_name='slideshowtest/test.html'):
    
    slideshow_slug = 'test'
    
    return render_to_response(template_name, locals(), RequestContext(request))


def mobile(request, template_name='slideshowtest/mobile.html'):
    
    slideshow_slug = 'test-mobile'
    
    return render_to_response(template_name, locals(), RequestContext(request))