# -*- coding: utf-8 -*-

import requests
from blinker import signal
from bs4 import BeautifulSoup


command = signal('command')
one = signal('1')
two = signal('2')


def make_request(sender):
    content = requests.get(sender.url).content
    soup = BeautifulSoup(content)
    return soup


def save_document(provider, title, href, image):
    from documents.models import Document

    try:
        Document.objects.get(href=href)
    except Document.DoesNotExist:
        doc = Document()
        doc.provider = provider
        doc.title = title
        doc.href = href
        doc.image = image
        doc.save()


@one.connect
def processOne(sender):
    soup = make_request(sender)
    itemList = soup.select('.flipbook')
    for item in itemList:
        title = item.get('alt')
        href = item.parent.get('href')
        image = item.get('data-path').replace('{index}', '2')
        save_document(sender, title, href, image)


@two.connect
def processsTwo(sender):
    soup = make_request(sender)
    itemList = soup.select('#miniatura')
    for item in itemList:
        title = item.find(id='title1').text
        href = item.find(class_='frame').get('href')
        image = item.find('img', class_='lazy').get('data-original')
        save_document(sender, title, href, image)
