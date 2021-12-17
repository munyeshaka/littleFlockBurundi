from django.shortcuts import render
from .models import *

def home(request):
    sermons = Sermon.objects.all().order_by('-date')[:3] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon
    articles = Article.objects.all().order_by('-date')[:3]
    videos = Video.objects.all().order_by('-date')[:2]
    return render(request,'flock/home.html', {'sermons':sermons, 'articles':articles, 'videos':videos}) #this flock is namespace help to differenciate with other home.html of other app's templates : is the fold inside of templates of the app #'sermons' receives sermons variable and it will be used in templates

def sermon_list(request):
    sermons = Sermon.objects.all().order_by('-date') #sermons variable receives data from db
    return render(request, 'flock/sermon_list.html', {'sermons':sermons}) #'sermons' receives sermons variable and it will be used in templates

def sermon_detail(request, slug):
    # #return HttpResponse(slug)
    # sermon = Sermon.objects.get(slug=slug)
    try:
        sermon = Sermon.objects.get(slug=slug)
    except Sermon.DoesNotExist:
        sermon = None
    return render(request, 'flock/sermon_detail.html', {'sermon':sermon})

def article_list(request):
    articles = Article.objects.all().order_by('-date') #articles variable receives data from db
    return render(request, 'flock/article_list.html', {'articles':articles}) #'articles' receives articles variable and it will be used in templates

def article_detail(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        article = None
    return render(request, 'flock/article_detail.html', {'article':article})