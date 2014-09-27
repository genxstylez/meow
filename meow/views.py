# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf import settings

from documents.models import Document, Category


def index(request):
    categories = Category.objects.order_by('-document')[:10]  # Sort by number of document associated
    documents = Document.objects.order_by('-views')[:1000]
    return render(request, 'index.html', {
        'categories': categories,
        'documents': documents,
        'site_title': settings.SITE_TITLE,
        'site_keywords': settings.SITE_KEYWORDS,
        'site_description': settings.SITE_DESCRIPTION,
        'site_brand': settings.SITE_BRAND,
        'site_slogan': settings.SITE_SLOGAN
    })
