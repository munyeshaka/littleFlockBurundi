from django.shortcuts import render
from .models import Sermon

def home(request):
    sermons = Sermon.objects.all().order_by('date') #sermons variable receives data from db
    return render(request,'flock/home.html', {'sermons':sermons}) #this flock is namespace help to differenciate with other home.html of other app's templates : is the fold inside of templates of the app #'sermons' receives sermons variable and it will be used in templates

def sermon_list(request):
    sermons = Sermon.objects.all().order_by('date') #sermons variable receives data from db
    return render(request, 'flock/sermon_list.html', {'sermons':sermons}) #'sermons' receives sermons variable and it will be used in templates

def sermon_detail(request, slug):
    #return HttpResponse(slug)
    sermon = Sermon.objects.get(slug=slug)
    return render(request, 'flock/sermon_detail.html', {'sermon':sermon})