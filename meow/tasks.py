# -*- coding: utf-8 -*-

from meow import celery_app
from providers.models import Provider


@celery_app.task
def add(x, y):
    return x + y

@celery_app.task
def crawl():
    for provider in Provider.objects.all():
        provider.get_contents()

