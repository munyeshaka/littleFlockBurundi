
from django.http import HttpResponse
from django.shortcuts import render
 
def home(request):
    #return HttpResponse('index')
    return render(request,'home.html')