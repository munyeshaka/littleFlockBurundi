

from django.urls import re_path

from .import views

app_name = 'flock'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),

    re_path(r'contacts/', views.sendMail, name='contacts'),
    re_path(r'flock/events/', views.events, name='events'),
    
    re_path('flock/success/', views.sendMail, name='success'),
    re_path(r'support_us/', views.support_us, name='support_us'),


    re_path(r'sermons/', views.sermon_list, name='sermons'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.sermon_detail, name='sermon_detail'),

    re_path(r'flock/articles/', views.article_list, name='articles'),
    re_path(r'flock/(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
    

]

