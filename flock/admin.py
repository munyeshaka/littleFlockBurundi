from django.contrib import admin
from .models import *
from django.utils.html import format_html


admin.site.site_header  =  "Little Flock Burundi admin"  
admin.site.site_title  =  "Little Flock Burundi admin site"
admin.site.index_title  =  "Little Flock Burundi Admin"

class AdminSermon(admin.ModelAdmin):

    # explicitly reference fields to be shown, note image_tag is read-only
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_tag.short_description = 'Photo'

    list_display = ['title', 'image_tag', 'body', 'date']

admin.site.register(Sermon,AdminSermon)


class AdminArticle(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_tag.short_description = 'Photo'
    list_display = ['title', 'image_tag', 'body', 'date']

admin.site.register(Article,AdminArticle)


class AdminVideo(admin.ModelAdmin):
    list_display = ['youtube_link', 'date']
admin.site.register(Video,AdminVideo)

class AdminEvent(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_tag.short_description = 'Photo'
    list_display = ['title', 'image_tag', 'description', 'expiration_date', 'expired']
admin.site.register(Event,AdminEvent)


