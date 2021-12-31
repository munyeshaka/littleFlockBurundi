from django.contrib import admin
from .models import *
from django.utils.html import format_html


admin.site.site_header  =  "Little Flock Burundi admin"  
admin.site.site_title  =  "Little Flock Burundi admin site"
admin.site.index_title  =  "Little Flock Burundi Admin"


class AdminSermon(admin.ModelAdmin):

    # explicitly reference fields to be shown, note photo_preview is read-only
    # def photo_preview(self, obj):
    #     return format_html('<img src="{}" width="200" height="auto" />'.format(obj.photo.url))
    # photo_preview.short_description = 'Photo Preview'
    # photo_preview.allow_tags = True
    # readonly_fields = ('photo_preview',)


    def image_in_table(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_in_table.short_description = 'Photo'
    image_in_table.allow_tags = True

    list_display = ['title', 'image_in_table', 'body', 'date']
    

admin.site.register(Sermon,AdminSermon)


class AdminArticle(admin.ModelAdmin):
    def image_in_table(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_in_table.short_description = 'Photo'
    list_display = ['title', 'image_in_table', 'body', 'date']

admin.site.register(Article,AdminArticle)


class AdminVideo(admin.ModelAdmin):
    list_display = ['youtube_link', 'date']
admin.site.register(Video,AdminVideo)


class AdminEvent(admin.ModelAdmin):
    def image_in_table(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_in_table.short_description = 'Photo'
    list_display = ['title', 'image_in_table', 'description', 'expiration_date', 'expired']
admin.site.register(Event,AdminEvent)


class AdminTeam(admin.ModelAdmin):
    def image_in_table(self, obj):
        return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))

    image_in_table.short_description = 'Photo'
    list_display = ['full_Name', 'image_in_table', 'service', 'email', 'phone_1', 'phone_2']
admin.site.register(Team,AdminTeam)