# -*- coding: utf-8 -*-

from meow import celery_app

from providers.models import Provider


@celery_app.task
def add(x, y):
    return x + y


def crawl():
    print '123'
    for provider in Provider.objects.all():
        provider.get_contents()
