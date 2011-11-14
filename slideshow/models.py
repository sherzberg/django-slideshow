from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.conf import settings

import tarfile,os,Image

SLIDESHOW_DIR = 'slideshow'

def gen_slideshowimage_upload_dir_func(subdir_name):
    '''
    Helper so we have consistant file uploads for filefields upload_to kwarg.
    '''
    def wrapper(instance, filename):
        path = '%s/%s/%s/%s' %(SLIDESHOW_DIR, instance.slideshow.slug, subdir_name, filename.replace(' ','-'))
        return path
    return wrapper

class Slideshow(models.Model):
    SLIDESHOW_TYPE_FLASH = 'flash'
    SLIDESHOW_TYPE_JAVASCRIPT_MOBILE = 'javascript-mobile'
    SLIDESHOW_TYPES = (
                       (SLIDESHOW_TYPE_FLASH, 'Flash'),
                       (SLIDESHOW_TYPE_JAVASCRIPT_MOBILE, 'Javascript Mobile'),)

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

    music_file = models.FileField(blank=True,upload_to=gen_slideshowimage_upload_dir_func('music'))
    music_loop = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view_slideshow', (), {'slideshow_slug': self.slug})
    
    @models.permalink
    def settings_url(self):
        return ('slideshow_settings', (), {'slideshow_slug': self.slug})

    def images(self):
        return self.slideshowimage_set.all()

class SlideshowImage(models.Model):

    image = models.FileField(blank=False,upload_to=gen_slideshowimage_upload_dir_func('images'))
    caption = models.CharField(blank=True, max_length=25)
    slideshow = models.ForeignKey(Slideshow, blank=False)

    def __unicode__(self):
        return str(self.slideshow) + ": " + self.caption
    
    def get_caption(self):
        if len(self.caption) > 0:
            return self.caption
        else:
            return self.image.url.split('/')[-1]

    def admin_thumbnail(self):
        if self.image:
            return u'<div style="text-align:center;"><img src="%s" height="100"></div>' % (self.image.url)
        else:
            return u'No image...'
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True
    
class SlideshowUpload(models.Model):
    tar_file = models.FileField('images file (.tar.gz)', upload_to=gen_slideshowimage_upload_dir_func('uploads'),
                                help_text='Select a .zip file of images to upload into a new Slideshow.')
    slideshow = models.ForeignKey(Slideshow, null=False, blank=False, help_text='Select a slideshow to add these images to. leave this empty to create a new gallery from the supplied title.')
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'slideshow upload'
        verbose_name_plural = 'slideshow uploads'

    def __unicode__(self):
        return str(self.slideshow) + ': ' + self.tar_file.path
    
    def save(self, *args, **kwargs):
        super(SlideshowUpload, self).save(*args, **kwargs)
        slideshow = self.process_tarfile()
        return slideshow

    def process_tarfile(self):
        if os.path.isfile(self.tar_file.path):
            tar = tarfile.open(self.tar_file.path,'r')
            
            for name in tar.getnames():
                
                slideshow_image = SlideshowImage(
                                  caption=name,
                                  slideshow=self.slideshow
                                  )
                file_path = gen_slideshowimage_upload_dir_func('images')(slideshow_image, name)
                
                slideshow_image.image = file_path
                slideshow_image.save()
                
                f = tar.extractfile(name)
                of = open(settings.MEDIA_ROOT+file_path,"w")
                of.write(f.read())
                of.close()
                
#TODO: check file to make sure its an image
#                data = zip.read(filename)
#                if len(data):
#                    try:
#                        # the following is taken from django.newforms.fields.ImageField:
#                        #  load() is the only method that can spot a truncated JPEG,
#                        #  but it cannot be called sanely after verify()
#                        trial_image = Image.open(StringIO(data))
#                        trial_image.load()
#                        # verify() is the only method that can spot a corrupt PNG,
#                        #  but it must be called immediately after the constructor
#                        trial_image = Image.open(StringIO(data))
#                        trial_image.verify()
#                    except Exception:
#                        # if a "bad" file is found we just skip it.
#                        continue
#                    while 1:
#                        title = ' '.join([self.title, str(count)])
#                        slug = slugify(title)
#                        try:
#                            p = Photo.objects.get(title_slug=slug)
#                        except Photo.DoesNotExist:
#                            photo = Photo(title=title,
#                                          title_slug=slug,
#                                          caption=self.caption,
#                                          is_public=self.is_public,
#                                          tags=self.tags)
#                            photo.image.save(filename, ContentFile(data))
#                            gallery.photos.add(photo)
#                            count = count + 1
#                            break
#                        count = count + 1
#            zip.close()
            return self.slideshow