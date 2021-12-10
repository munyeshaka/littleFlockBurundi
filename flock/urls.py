#from django.urls import path, re_path
#from django.conf.urls import url
from django.urls import re_path

from .import views

app_name = 'flock'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'programs/', views.sermon_list, name='programs'),
    re_path(r'sermons/', views.sermon_list, name='sermons'),
    re_path(r'articles/', views.sermon_list, name='articles'),
    re_path(r'videos/', views.sermon_list, name='videos'),
    re_path(r'events/', views.sermon_list, name='events'),
    re_path(r'support_us/', views.sermon_list, name='support_us'),
    re_path(r'contact/', views.sermon_list, name='contact'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.sermon_detail, name='sermon_detail'),
]

