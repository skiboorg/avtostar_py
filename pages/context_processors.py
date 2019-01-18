from .models import Service


def get_all_services(request):
    main_services = Service.objects.filter(is_main_service=True)
    other_services = Service.objects.filter(is_main_service=False)

    return locals()