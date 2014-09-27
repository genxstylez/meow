# -*- coding: utf-8 -*-

from meow import celery_app
from providers.models import Provider
from documents.models import Document
from providers.signals import make_request


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def crawl():
    for provider in Provider.objects.all():
        provider.get_contents()

    #keep = Document.objects.order_by('-views')[:1000].values_list('id', flat=True)
    #Document.objects.exclude(pk__in=list(keep)).delete()
    # Keep the 1000 most viewed


@celery_app.task
def refresh_embed():
    documents = Document.objects.all()
    for document in documents:
        soup = make_request(document.href, mobile=True)
        try:
            if document.provider.codename == 'RT':
                embed = soup.select('div#html5_vid a')[0].get('href')
            elif document.provider.codename == 'YJ':
                embed = soup.select('a.preview_thumb')[0].get('href')

            document.embed = embed
            document.save()
        except IndexError:
            document.delete()
