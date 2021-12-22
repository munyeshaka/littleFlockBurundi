from django.shortcuts import render
from .models import *

from django.shortcuts import render, redirect
from .forms import ContactMeForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


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
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, "flock/success.html")
    return render(request, 'flock/contacts.html', {'form':form})

def support_us(request):
    articles = Article.objects.all().order_by('-date') #articles variable receives data from db
    return render(request, 'flock/support_us.html', {'articles':articles}) #'articles' 

def events(request):
    articles = Article.objects.all().order_by('-date') #articles variable receives data from db
    return render(request, 'flock/events.html', {'articles':articles}) #'articles'