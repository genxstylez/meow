# -*- coding: utf-8 -*-

import urlparse

from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect

from providers.signals import make_request
from documents.models import Document, Category


def document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    provider = document.provider
    try:
        if provider.codename == 'RT':
            soup = make_request(document.href, mobile=True)
            embed = soup.select('div#html5_vid a')[0].get('href')
        elif provider.codename == 'YJ':
            mobile_href = urlparse.urljoin(provider.mobile_url, document.href.strip(provider.url))
            mobile_soup = make_request(mobile_href)
            embed = mobile_soup.select('a.preview_thumb')[0].get('href')

        document.embed = embed
        document.save()
    except IndexError:
        raise Http404

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
