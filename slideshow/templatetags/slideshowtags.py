
from django import template
from django.shortcuts import get_object_or_404, render_to_response
from slideshow.models import Slideshow
from django.conf import settings

register = template.Library()

class SlideshowRenderer(template.Node):
    
    def __init__(self, slideshow):
        try:
            self.slideshow = get_object_or_404(Slideshow, id=slideshow.id)
        except:
            self.slideshow = get_object_or_404(Slideshow, slug=slideshow)
        
    def render(self, context):
        setattr(context, 'slideshow',self.slideshow)
        setattr(context, 'images',self.slideshow.images())
        
        d = {
             'MEDIA_URL': settings.MEDIA_URL,
             'slideshow': self.slideshow
             }
        t = template.loader.get_template('slideshow/slideshow.html')
        c = template.Context(d)
        
        html = t.render(c)
        
        return html
    
    
def do_slideshow(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, slideshow_slug = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
    if not (slideshow_slug[0] == slideshow_slug[-1] and slideshow_slug[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    
    return SlideshowRenderer(slideshow_slug[1:-1])

register.tag('slideshow', do_slideshow)