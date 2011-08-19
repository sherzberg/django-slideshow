from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Slideshow(models.Model):
    SLIDESHOW_TYPE_FLASH = 'flash'    
    SLIDESHOW_TYPES = ((SLIDESHOW_TYPE_FLASH, 'Flash'),)

    name = models.CharField(blank=False, max_length=50)
    slug = models.SlugField(blank=False, max_length=50)
    type = models.CharField(choices=SLIDESHOW_TYPES, default=SLIDESHOW_TYPE_FLASH, max_length=20)

    height = models.IntegerField(blank=False)
    width = models.IntegerField(blank=False)

    auto_play = models.BooleanField(default=True)
    loop_play = models.BooleanField(default=True)
    random = models.BooleanField(default=True)
    display_time = models.DecimalField(blank=False, decimal_places=3, max_digits=5)    
    transition_speed = models.DecimalField(blank=False, decimal_places=3, max_digits=5)

    music_file = models.FileField(blank=True,upload_to='slideshow_music')
    music_loop = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def settings_url(self):
        return reverse('slideshow_settings', args=[self.slug])

    def images(self):
        return self.slideshowimage_set.all()
    
class SlideshowImage(models.Model):

    image = models.FileField(blank=False,upload_to='slideshow_images')
    caption = models.CharField(blank=True, max_length=25)
    slideshow = models.ForeignKey(Slideshow, blank=False)

    def __unicode__(self):
        return str(self.slideshow) + ": " + self.caption
    
    
