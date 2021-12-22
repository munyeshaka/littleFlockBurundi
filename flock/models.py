from django.db import models
#from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify # for auto-slug _  #pip install python-slugify
import datetime
from django.conf import settings


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


class Article(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', default='default.png', blank=True)
    # title slug date body thumb

    def __str__(self):
        return self.title
    
    def save(self): # for auto-slug __   date and title
        super(Article, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title)
        )
        super(Article, self).save()

    def snippet(self):
        return self.body[:100] +'...'

class Video(models.Model):
    youtube_link = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.youtube_link
    
    def save(self): # for auto-slug __   date and title
        super(Video, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.youtube_link)
        )
        super(Video, self).save()

    def snippet(self):
        return self.youtube_link[-11:] #to get youtube id of link


class Event(models.Model):

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    in_progress = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    duration = models.PositiveIntegerField(default=15)
    #title description in_progress created_at updated_at expiration_date duration

    def save(self, *args, **kw):
            ## your custom date logic to verify if expired or not.
            if self.expiration_date < datetime.datetime.now().date():
                self.in_progress = False
            super(Event, self).save(*args, **kw)




