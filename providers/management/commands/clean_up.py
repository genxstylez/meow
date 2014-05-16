# -*- coding: utf-8 -*-
import urlparse
from django.core.management.base import BaseCommand
from providers.models import Provider
from providers.signals import make_request
from documents import Image


class Command(BaseCommand):
    def handle(self, **options):
        xh = Provider.objects.get(codename='XH')
        xh_docs = xh.document_set.all()
        xh_docs.delete()

        yj = Provider.objects.get(codename='YJ')
        yj_docs = yj.document_set.all()
        yj_docs[500:].delete()

        for doc in yj_docs:
            soup = make_request(doc.href)
            image_url = soup.find('img', class_='lazy').get('data-original')
            for i in range(2, 9):
                image = Image()
                image.url = image_url.replace('flv-1', 'flv-%s' % i)
                image.document = doc
                image.save()

            mobile_href = urlparse.urljoin(yj.mobile_url, soup.find(class_='frame').get('href'))

            mobile_soup = make_request(mobile_href)

            embed = mobile_soup.select('a.preview_thumb')[0].get('href')

            doc.embed = embed

            doc.save()
            