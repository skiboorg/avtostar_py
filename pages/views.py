from django.shortcuts import render
from pages.models import Service , Banner, Image
import glob
import os
from avtostar.settings import STATIC_URL

def index(request):
    active_home = 'active'
    title = 'ТЕХНИЧЕСКИЙ ЦЕНТР '
    banners = Banner.objects.filter(is_active=True).order_by('order')
    services = Service.objects.filter(show_at_home=True)
    images = Image.objects.all()


    return render(request, 'pages/index.html', locals())

def service(request,name_slug):
    active_service = 'active'

    service = Service.objects.get(name_slug=name_slug)
    title = service.name


    return render(request, 'pages/service.html', locals())

def avtomasla(request):
    active_shop = 'active'
    directory = 'static/images/brands/*'


    files = glob.glob(directory)
    print(files)
    title = 'КАТАЛОГ АВТОМОБИЛЬНЫХ МАСЕЛ, ТОСОЛОВ И АНТИФРИЗОВ, АВТОХИМИИ И АВТОКОСМЕТИКИ'
    return render(request, 'pages/avtomasla.html', locals())
