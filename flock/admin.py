from django.contrib import admin
from .models import *

admin.site.site_header  =  "Little Flock Burundi admin"  
admin.site.site_title  =  "Little Flock Burundi admin site"
admin.site.index_title  =  "Little Flock Burundi Admin"

class AdminSermon(admin.ModelAdmin):
    list_display = ['title', 'photo', 'body', 'date']
    
    # # explicitly reference fields to be shown, note image_tag is read-only
    # fields = ('title', 'image_tag', 'body',)
    # readonly_fields = ('image_tag',)


admin.site.register(Sermon,AdminSermon)
