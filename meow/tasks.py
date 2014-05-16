# -*- coding: utf-8 -*-

from meow import celery_app
from providers.models import Provider
from documents.models import Document


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def crawl():
    for provider in Provider.objects.all():
        provider.get_contents()

    keep = Document.objects.order_by('-views')[1000:].values_list('id', flat=True)
    Document.objects.exclude(pk__in=list(keep)).delete()
    # Keep the 1000 most viewed
