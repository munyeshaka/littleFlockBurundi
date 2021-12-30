

from django.urls import re_path

from .import views


app_name = 'flock_kirundi'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'flock_kirundi/homeKir/', views.homeKir, name='homeKir'),
    re_path(r'flock_kirundi/aboutKir', views.aboutKir, name='aboutKir'),

    re_path(r'flock_kirundi/contactsKir/', views.sendMailKir, name='contactsKir'),
    re_path(r'flock_kirundi/eventsKir/', views.eventsKir, name='eventsKir'),
    
    re_path(r'flock_kirundi/successKir/', views.sendMailKir, name='successKir'),
    re_path(r'flock_kirundi/support_usKir/', views.support_usKir, name='support_usKir'),


    re_path(r'flock_kirundi/sermonsKir/', views.sermon_listKir, name='sermonsKir'),
    re_path(r'^/(?P<slug>[\w-]+)/$', views.sermon_detailKir, name='sermon_detailKir'),

    re_path(r'flock_kirundi/articlesKir/', views.article_listKir, name='articlesKir'),
    re_path(r'flock_kirundi/(?P<slug>[\w-]+)/$', views.article_detailKir, name='article_detailKir'),

    
]

