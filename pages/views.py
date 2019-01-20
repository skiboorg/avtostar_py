from django.shortcuts import render
from pages.models import Service , Banner, Image

def index(request):
    banners = Banner.objects.filter(is_active=True).order_by('order')
    services = Service.objects.filter(show_at_home=True)
    images = Image.objects.all()


    return render(request, 'pages/index.html', locals())

def service(request,name_slug):
    service = Service.objects.get(name_slug=name_slug)



    return render(request, 'pages/service.html', locals())
