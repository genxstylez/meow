# -*- coding: utf-8 -*-

import celery
from datetime import timedelta
from celery.decorators import periodic_task

from providers.models import Provider


@celery.task
def add(x, y):
    return x + y


@periodic_task(run_every=timedelta(hours=1))
def crawl():
    for provider in Provider.objects.all():
        provider.get_contents()
