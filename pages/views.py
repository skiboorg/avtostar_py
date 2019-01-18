from django.shortcuts import render
from pages.models import Service

def index(request):


    return render(request, 'pages/index.html', locals())

def service(request,name_slug):
    service = Service.objects.get(name_slug=name_slug)



    return render(request, 'pages/service.html', locals())
