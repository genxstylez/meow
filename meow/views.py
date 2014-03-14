# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings

from documents.models import Document


def index(request):
    documents = Document.objects.order_by('-hits')
    return render(request, 'index.html', {
        'documents': documents,
        'site_title': settings.SITE_TITLE,
        'site_keywords': settings.SITE_KEYWORDS,
        'site_description': settings.SITE_DESCRIPTION,
        'site_brand': settings.SITE_BRAND,
        'site_slogan': settings.SITE_SLOGAN
    })
