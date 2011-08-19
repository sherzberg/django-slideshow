from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import Template, Context, RequestContext
from django.template.loader import get_template

from slideshow.models import Slideshow, SlideshowImage

def view_slideshow(request, slideshow_slug, template_name='slideshow/slideshow.html'):
    slideshow = get_object_or_404(Slideshow, slug=slideshow_slug)
    images = slideshow.images()
    
    return render_to_response(template_name, locals(), RequestContext(request))


def slideshow_settings(request, slideshow_slug, template_name='slideshow/settings.xml'):
    slideshow = get_object_or_404(Slideshow, slug=slideshow_slug)
    images = slideshow.images()

    template = get_template('slideshow/settings.xml')
    context = Context({'slideshow': slideshow, 'images': images})
    
    return render_to_response(template_name, locals(), RequestContext(request))
