from django.contrib import admin

from slideshow.models import SlideshowImage, Slideshow, SlideshowUpload

class SlideshowImageInline(admin.TabularInline):
    model = SlideshowImage
    
class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', )
    list_filter = ('type',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SlideshowImageInline]
    list_per_page = 25
    fieldsets = (
        (None, {
            'fields': (
                       ('name', 'slug', ),
                       'type',
                       ('width', 'height'),
                       )
        }),
        ('Play options', {
            'fields': (
                       ('auto_play', 'loop_play', 'random',),
                       'display_time',
                       'transition_speed',
                       )
        }),
        ('Music options', {
            'fields': (
                       'music_file',
                       'music_loop',
                       )
        }),
    )

class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'slideshow', 'admin_thumbnail',)
    list_filter = ('slideshow',)
    list_per_page = 50

class SlideshowUploadAdmin(admin.ModelAdmin):
    list_display = ('slideshow', 'tar_file', )
    list_filter = ('slideshow',)
    
admin.site.register(SlideshowImage, SlideshowImageAdmin)
admin.site.register(Slideshow, SlideshowAdmin)
admin.site.register(SlideshowUpload, SlideshowUploadAdmin)
