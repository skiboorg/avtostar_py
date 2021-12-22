from django.shortcuts import render
from pages.models import Service , Banner, Image
import glob

from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(request):
    if request.POST:
        send_mail('Запрос на обратный звонок', 'Посетитель {} просит перезвонить ему на номер {} '.format(
            request.POST.get('name'),request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True
    active_home = 'active'
    title = 'РЕМОНТ АВТОМОБИЛЕЙ ВСЕХ МАРОК'
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


def about(request):
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

def corruption(request):
    if request.POST:
        send_mail('Новый отзыв', 'Посетитель {} по поводу сервиса {} поставил оценку {}. Тескт сообщения: {} . Телефон: {} '.format(
            request.POST.get('name'),
            request.POST.get('service'),
            request.POST.get('rating'),
            request.POST.get('message'),
            request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        send = True

    title = 'Противодействие коррупции'
    return render(request, 'pages/korruptsiya.html', locals())

def ladadetal(request):

    active_shop = 'active'
    title = 'КУПИТЬ ОРИГИНАЛЬНЫЕ ЗАПЧАСТИ ЛАДА'
    return render(request, 'pages/lada.html', locals())


def avtodj(request):
    if request.POST:
        # test_txt = 'тестттт'
        # msg_plain = render_to_string('email.txt', {'text': test_txt})
        # msg_html = render_to_string('test_email.html', {'text': test_txt})
        send_mail('Запрос на обратный звонок', 'Посетитель {} просит перезвонить ему на номер {} '.format(
            request.POST.get('name'), request.POST.get('phone')), 'admin@avtostar-kmv.ru', ['marketing@avtostar-kmv.ru'], fail_silently=False)
        # send_mail('Запрос на обратный звонок',None, 'noreply@yandex.ru', ['marketing@avtostar-kmv.ru'],
        #           fail_silently=False, html_message=msg_html)
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


