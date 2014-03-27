# -*- coding: utf-8 -*-

import requests
import locale
from blinker import signal
from bs4 import BeautifulSoup


command = signal('command')
one = signal('1')


def make_request(url):
    content = requests.get(url).content
    soup = BeautifulSoup(content)
    return soup


def save_document(provider, title, href, image, embed, desc, duration, views, categories):
    from documents.models import Document, Category

    try:
        Document.objects.get(href=href)
    except Document.DoesNotExist:
        doc = Document()
        doc.provider = provider
        doc.title = title
        doc.href = href
        doc.image = image
        doc.embed = embed
        doc.desc = desc
        doc.duration = duration
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        doc.views = locale.atoi(views)
        doc.save()

        for category in categories:
            cat = Category.objects.get_or_create(title=category.text)
            doc.categories.add(cat[0])

"""
DEPRECATED
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
"""


@one.connect
def processOne(sender):
    soup = make_request(sender.url)
    itemList = soup.select('div.video')
    for item in itemList:
        title = item.select('u')[0].text
        image = item.select('img')[0].get('src')
        href = item.select('a')[0].get('href')

        # Here we make second request
        second_soup = make_request(href)
        embed = second_soup.select('div#shareBox')[0].select('iframe')[0]
        try:
            desc = second_soup.select('div#videoInfoBox')[0].select('td.desc')[0].text.strip('Description: ')
        except IndexError:
            desc = ''
        duration = second_soup.select('div#videoInfoBox')[0].select('td#videoUser')[0].select('.item')[1].text.strip('Runtime: ')
        views = second_soup.select('div#videoInfoBox')[0].select('td#videoUser')[0].select('.item')[2].text.strip('Views: ')
        categories = second_soup.select('div#videoInfoBox')[0].select('#channels a')

        save_document(sender, title, href, image, embed, desc, duration, views, categories)
