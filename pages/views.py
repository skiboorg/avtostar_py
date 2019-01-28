from django.shortcuts import render
from pages.models import Service , Banner, Image
import glob
import os
from avtostar.settings import STATIC_URL
from django.core.mail import send_mail

def index(request):
    if request.POST:
        send_mail('Запрос на обратный звонок', 'Посетитель {} просит перезвонить ему на номер {} '.format(
            request.POST.get('name'),request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True
    active_home = 'active'
    title = 'ТЕХНИЧЕСКИЙ ЦЕНТР '
    banners = Banner.objects.filter(is_active=True).order_by('order')
    services = Service.objects.filter(show_at_home=True)
    images = Image.objects.all()


    return render(request, 'pages/index.html', locals())

def service(request,name_slug):
    active_service = 'active'
    if name_slug == 'all':
        all_services = Service.objects.filter(is_main_service=True)
        title = "УСЛУГИ АВТОСЕРВИСА"
        return render(request, 'pages/service_all.html', locals())
    else:
        service = Service.objects.get(name_slug=name_slug)
        title = service.name
        return render(request, 'pages/service.html', locals())


def contact(request):
    if request.POST:
        send_mail('Новый отзыв', 'Посетитель {} по поводу сервиса {} поставил оценку {}. Тескт сообщения: {} . Телефон: {} '.format(
            request.POST.get('name'),
            request.POST.get('service'),
            request.POST.get('rating'),
            request.POST.get('message'),
            request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True
    active_contact = 'active'
    title = 'НАШИ КОНТАКТЫ'
    return render(request, 'pages/contact.html', locals())

def ladadetal(request):

    active_shop = 'active'
    title = 'КУПИТЬ ОРИГИНАЛЬНЫЕ ЗАПЧАСТИ ЛАДА ПО ВЫГОДНЫМ ЦЕНАМ В ПЯТИГОРСКЕ И КМВ. КАТАЛОГ ЗАПЧАСТЕЙ ВАЗ ВСЕХ МОДЕЛЕЙ В НАЛИЧИИ И ПОД ЗАКАЗ'
    return render(request, 'pages/lada.html', locals())

def avtodj(request):
    if request.POST:
        send_mail('Запрос на обратный звонок', 'Посетитель {} просит перезвонить ему на номер {} '.format(
            request.POST.get('name'),request.POST.get('phone')), 'noreply@yandex.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True
    directory = 'static/images/djbrands/*'
    files = glob.glob(directory)
    active_shop = 'active'
    title = 'МАГАЗИН АВТОЭЛЕКТРОНИКИ АВТОDJ'
    return render(request, 'pages/avtodj.html', locals())

def avtomasla(request):
    if request.POST:
        send_mail('Запрос на обратный звонок', 'Посетитель {} просит перезвонить ему на номер {} по поводу автомасел'.format(
            request.POST.get('name'),request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True
    active_shop = 'active'
    directory = 'static/images/brands/*'
    files = glob.glob(directory)
    print(files)
    title = 'КАТАЛОГ АВТОМОБИЛЬНЫХ МАСЕЛ, ТОСОЛОВ И АНТИФРИЗОВ, АВТОХИМИИ И АВТОКОСМЕТИКИ'
    return render(request, 'pages/avtomasla.html', locals())


