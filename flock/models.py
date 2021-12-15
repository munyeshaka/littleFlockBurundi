from django.db import models
#from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify # for auto-slug _  #pip install python-slugify
import datetime
from django.conf import settings
import os
from django.utils.safestring import mark_safe


# Create your models here.


class Sermon(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', default='default.png', blank=True)
    # title slug date body thumb

    def __str__(self):
        return self.title
    
    def save(self): # for auto-slug __   date and title
        super(Sermon, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title)
        )
        super(Sermon, self).save()

    def snippet(self):
        return self.body[:100] +'...'


    
    # #display image in admin
    # def image_tag(self):
    #     # used in the admin site model as a "thumbnail"
    #     return mark_safe('<img src="{}" width="150" height="150" />'.format(self.photo) )
    # image_tag.short_description = 'Image'
