#from django.urls import path, re_path
#from django.conf.urls import url
from django.urls import re_path

from .import views

app_name = 'flock'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'sermons/', views.sermon_list, name='sermons'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.sermon_detail, name='sermon_detail'),
]

