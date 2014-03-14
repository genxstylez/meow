# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from documents.models import Document


def document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    return render(request, 'document.html', {
        'document': document,
        'site_title': settings.SITE_TITLE,
        'site_brand': settings.SITE_BRAND,
        'site_slogan': settings.SITE_SLOGAN}
    )
