from django.shortcuts import render
from flock.models import *
from flock_kirundi.models import *
from .forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def countEventsKir(request):
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock_kirundi/base_layoutKir.html', {'upcomingEventsKir':upcomingEventsKir}) #'articlesKir'

def home(request):
    sermons = Sermon.objects.all().order_by('-date')[:3] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon
    articles = Article.objects.all().order_by('-date')[:3]
    videos = Video.objects.all().order_by('-date')[:2]
    upcomingEventss = Event.objects.all().filter(expired = False).order_by('expiration_date')[:1]
    upcomingEvents = Event.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock/home.html', {'sermons':sermons, 'articles':articles, 'videos':videos, 'upcomingEventssKir':upcomingEventss, 'upcomingEvents':upcomingEvents}) 
    #this flock_kirundi is namespace help to differenciate with other home.html of other app's templates : is the fold inside of templates of the app #'sermons' receives sermons variable and it will be used in templates
def homeKir(request):
    sermonsKir = KirundiSermon.objects.all().order_by('-date')[:3] #sermons variable receives data from db    ### ...(-date)[:3] _last 3 sermon
    articlesKir = KirundiArticle.objects.all().order_by('-date')[:3]
    videosKir = KirundiVideo.objects.all().order_by('-date')[:2]
    upcomingEventssKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')[:1]
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock_kirundi/homeKir.html', {'sermonsKir':sermonsKir, 'articlesKir':articlesKir, 'videos':videosKir, 'upcomingEventssKir':upcomingEventssKir, 'upcomingEventsKir':upcomingEventsKir})

def aboutKir(request):
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request,'flock_kirundi/aboutKir.html', {'upcomingEventsKir':upcomingEventsKir})


def sermon_listKir(request):
    sermonsKir = KirundiSermon.objects.all().order_by('-date') #sermons variable receives data from db
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/sermon_listKir.html', {'sermonsKir':sermonsKir, 'upcomingEventsKir':upcomingEventsKir}) #'sermons' receives sermons variable and it will be used in templates


def sermon_detailKir(request, slug):
    # #return HttpResponse(slug)
    # sermon = Sermon.objects.get(slug=slug)
    try:
        sermonKir = KirundiSermon.objects.get(slug=slug)
    except KirundiSermon.DoesNotExist:
        sermonKir = None
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/sermon_detailKir.html', {'sermonKir':sermonKir, 'upcomingEventsKir':upcomingEventsKir})


def article_listKir(request):
    articlesKir = KirundiArticle.objects.all().order_by('-date')
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/article_listKir.html', {'articlesKir':articlesKir, 'upcomingEventsKir':upcomingEventsKir}) #'articlesKir' receives articlesKir variable and it will be used in templates


def article_detailKir(request, slug):
    try:
        articleKir = KirundiArticle.objects.get(slug=slug)
    except KirundiArticle.DoesNotExist:
        articleKir = None
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/article_detailKir.html', {'articleKir':articleKir, 'upcomingEventsKir':upcomingEventsKir})


def sendMailKir(request):
    form = ContactMeForm()
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            # form.save()
            # send_mail(subject, message[fname, lname, email, phonenumber, subject, message], sedner, recipient)
            subject = "Message from Little flock Websibe"
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
                upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "flock_kirundi/successKir.html", {'upcomingEventsKir':upcomingEventsKir})

    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/contactsKir.html', {'form':form, 'upcomingEventsKir':upcomingEventsKir})

def successKir(request):
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock_kirundi/successKir.html', {'upcomingEventsKir':upcomingEventsKir})

def support_usKir(request):
    teams = Team.objects.all() 
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
    return render(request, 'flock_kirundi/support_usKir.html', {'upcomingEventsKir':upcomingEventsKir, 'teams':teams}) #'articlesKir' 

def eventsKir(request):
    upcomingEventsKir = KirundiEvent.objects.all().filter(expired = False).order_by('expiration_date')
     #upcoming variable receives data from db witch is not expired
    return render(request, 'flock_kirundi/eventsKir.html', {'upcomingEventsKir':upcomingEventsKir}) 