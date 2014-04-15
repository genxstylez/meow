# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from documents.models import Document, Category


def document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    return render(request, 'document.html', {
        'document': document,
        'site_title': settings.SITE_TITLE,
        'site_brand': settings.SITE_BRAND,
        'site_slogan': settings.SITE_SLOGAN}
    )


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    documents = category.docs.all()

    return render(request, 'category.html', {
        'category': category,
        'documents': documents,
        'site_title': settings.SITE_TITLE,
        'site_brand': settings.SITE_BRAND,
        'site_slogan': settings.SITE_SLOGAN}
    )


@csrf_protect
def hits(request, document_id):
    if request.is_ajax():
        doc = get_object_or_404(Document, id=document_id)
        doc.views += 1
        doc.save()
        return HttpResponse(200)

    return HttpResponse(403)
