from django.shortcuts import render
from flock.models import *
from flock_kirundi.models import *
from .forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def countEvents(request):
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock/base_layout.html', {'upcomingEvents':upcomingEvents}) #'articles'

def home(request):
    sermons = Sermon.objects.all().order_by('-date')[:3] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon
    articles = Article.objects.all().order_by('-date')[:3]
    videos = Video.objects.all().order_by('-date')[:2]
    upcomingEventss = Event.objects.all().filter(expired = False).order_by('expiration_date')[:1]
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock/home.html', {'sermons':sermons, 'articles':articles, 'videos':videos, 'upcomingEventss':upcomingEventss, 'upcomingEvents':upcomingEvents}) 
    #this flock is namespace help to differenciate with other home.html of other app's templates : is the fold inside of templates of the app #'sermons' receives sermons variable and it will be used in templates
def homeKir(request):
    sermonsKir = KirundiSermon.objects.all().order_by('-date')[:3] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon
    articlesKir = KirundiArticle.objects.all().order_by('-date')[:3]
    videos = Video.objects.all().order_by('-date')[:2]
    upcomingEventssKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')[:1]
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock_kirundi/homeKir.html', {'sermonsKir':sermonsKir, 'articlesKir':articlesKir, 'videos':videos, 'upcomingEventssKir':upcomingEventssKir, 'upcomingEventsKir':upcomingEventsKir})

def about(request):
    upcomingEvents = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock/about.html', {'upcomingEvents':upcomingEvents})

def sermon_list(request):
    sermons = Sermon.objects.all().order_by('-date') #sermons variable receives data from db
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock/sermon_list.html', {'sermons':sermons, 'upcomingEvents':upcomingEvents}) #'sermons' receives sermons variable and it will be used in templates


def sermon_detail(request, slug):
    # #return HttpResponse(slug)
    # sermon = Sermon.objects.get(slug=slug)
    try:
        sermon = Sermon.objects.get(slug=slug)
    except Sermon.DoesNotExist:
        sermon = None
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')

    recentSermons = Sermon.objects.all().order_by('-date')[:5] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon

    return render(request, 'flock/sermon_detail.html', {'sermon':sermon, 'upcomingEvents':upcomingEvents, 'recentSermons':recentSermons})


def article_list(request):
    articles = Article.objects.all().order_by('-date') #articles variable receives data from db
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock/article_list.html', {'articles':articles, 'upcomingEvents':upcomingEvents}) #'articles' receives articles variable and it will be used in templates


def article_detail(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        article = None
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')

    recentArticles = Article.objects.all().order_by('-date')[:5]

    return render(request, 'flock/article_detail.html', {'article':article, 'upcomingEvents':upcomingEvents, 'recentArticles':recentArticles})


def sendMail(request):
    form = ContactMeForm()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)
            subject = "Message from Little Flock Websibe"
            body = {
                'email': form.cleaned_data['emailid'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            }
            message = '\n\n'.join(body.values())
            sender = form.cleaned_data['emailid']  #message from
            recipient = ['aimablemunyeshaka30@gmail.com'] # message to
            try:
                send_mail(subject, message, sender, recipient, fail_silently=True)
                upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "flock/success.html", {'upcomingEvents':upcomingEvents})

    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock/contacts.html', {'form':form, 'upcomingEvents':upcomingEvents})

def success(request):
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock/success.html', {'upcomingEvents':upcomingEvents})

def support_us(request):
    articles = Article.objects.all().order_by('-date') #articles variable receives data from db
    teams = Team.objects.all()
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock/support_us.html', {'articles':articles, 'upcomingEvents':upcomingEvents, 'teams':teams}) #'articles' 

def events(request):
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock/events.html', {'upcomingEvents':upcomingEvents}) 