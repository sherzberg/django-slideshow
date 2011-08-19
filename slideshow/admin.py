from django.contrib import admin

from slideshow.models import SlideshowImage, Slideshow

class SlideshowAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(SlideshowImage)
admin.site.register(Slideshow, SlideshowAdmin)
