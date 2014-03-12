# -*- coding: utf-8 -*-

import celery
import requests
from datetime import timedelta
from celery.decorators import periodic_task
from bs4 import BeautifulSoup

from documents.models import Document
from providers.models import Provider


@celery.task
def add(x, y):
    return x + y


@periodic_task(run_every=timedelta(hours=1))
def crawl():
    for provider in Provider.objects.all():
        content = requests.get(provider.url).content
        soup = BeautifulSoup(content)
        itemList = soup.select(provider.css_selector)
        for item in itemList:
            href = item.parent.get('href')

            try:
                Document.objects.get(rel_url=href)
            except Document.DoesNotExist:
                doc = Document()
                doc.provider = provider
                doc.title = item.get('alt')
                doc.rel_url = href
                doc.content = repr(item)
                doc.save()
