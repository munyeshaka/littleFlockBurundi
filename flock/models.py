from django.db import models
#from django.db.models.fields import SlugField
from django.template.defaultfilters import slugify # for auto-slug _  #pip install python-slugify
import datetime

# Create your models here.


class Sermon(models.Model):
    title = models.CharField(max_length=101)
    slug = models.SlugField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)
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
        return self.body[:200] +'...'
