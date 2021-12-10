from django.contrib import admin
from .models import *

admin.site.site_header  =  "Little Flock Burundi admin"  
admin.site.site_title  =  "Little Flock Burundi admin site"
admin.site.index_title  =  "Little Flock Burundi Admin"

class AdminSermon(admin.ModelAdmin):
    list_display = ['title', 'thumb', 'body', 'date']
admin.site.register(Sermon,AdminSermon)
