from django.db import models

# Create your models here.
from django.db import models
#from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify # for auto-slug _  #pip install python-slugify
import datetime
from django.conf import settings
from django.utils.html import format_html
from django.contrib.admin.decorators import display

# Create your models here.


class KirundiSermon(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', default='default.png', blank=True)
    # title slug date body thumb

    def __str__(self):
        return self.title
    
    def save(self): # for auto-slug __   date and title
        super(KirundiSermon, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title)
        )
        super(KirundiSermon, self).save()

    def snippet(self):
        return self.body[:100] +'...'



class KirundiArticle(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    # title slug date body thumb

    def __str__(self):
        return self.title
    
    def save(self): # for auto-slug __   date and title
        super(KirundiArticle, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.title)
        )
        super(KirundiArticle, self).save()

    def snippet(self):
        return self.body[:100] +'...'

class KirundiVideo(models.Model):
    youtube_link = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.youtube_link
    
    def save(self): # for auto-slug __   date and title
        super(KirundiVideo, self).save()
        date = datetime.datetime.now()
        self.slug = '%i-%i-%i-%s-%s-%s-%s' % (
            date.year, date.month, date.day, date.hour, date.minute, date.second, slugify(self.youtube_link)
        )
        super(KirundiVideo, self).save()

    def snippet(self):
        return self.youtube_link[-11:] #to get youtube id of link


class KirundiEvent(models.Model):

    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='%Y/%m/%d/', default='default.png', blank=True)
    description = models.CharField(max_length=300)
    expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    #title description expired created_at updated_at expiration_date duration

    def save(self, *args, **kw):
            ## your Kirundievent date logic to verify if expired or not.
            
        future_today_date = datetime.date.today()
        if self.expiration_date < future_today_date:
            self.expired = True
        if self.expiration_date > future_today_date:
            self.expired = False
        super(KirundiEvent, self).save(*args, **kw)

    def len(self):
        return self.expired(expired=True)




