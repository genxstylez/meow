from django.conf import settings


def all_meow(request):
    return {
        'JS_DEBUG': settings.JS_DEBUG if hasattr(settings, 'JS_DEBUG') else False,
        'SITE_SLOGAN': settings.SITE_SLOGAN if hasattr(settings, 'SITE_SLOGAN') else '',
        'SITE_BRAND': settings.SITE_BRAND if hasattr(settings, 'SITE_BRAND') else ''
    }
