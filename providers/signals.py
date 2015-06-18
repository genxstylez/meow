# -*- coding: utf-8 -*-

import requests
import locale
import urlparse
from blinker import signal
from bs4 import BeautifulSoup

one = signal('1')
two = signal('2')


def make_request(url, mobile=False):
    if mobile:
        content = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D)\
         AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}).content
    else:
        content = requests.get(url).content
    soup = BeautifulSoup(content)
    return soup


def save_document(provider, title, href, images, embed, desc, duration, views, categories):
    from documents.models import Document, Category, Image

    try:
        doc = Document.objects.get(href=href)
    except Document.DoesNotExist:
        doc = Document()
        doc.provider = provider
        doc.title = title
        doc.href = href
        doc.embed = embed
        doc.desc = desc
        doc.duration = duration

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    doc.views = locale.atoi(views)
    doc.save()
    
    if doc.images.count() == 0:
        for image_url in images:
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image()
                image.document = doc
                image.url = image_url
                image.save()

    for category in categories:
        cat = Category.objects.get_or_create(title=category)
        doc.categories.add(cat[0])


@one.connect
def processOne(sender):
    soup = make_request(sender.url)
    itemList = soup.select('a.video-thumb')
    for item in itemList:
        title = item.get('title')
        image = item.select('img')[0].get('src')
        href = urlparse.urljoin(sender.url, item.get('href'))
        duration = item.select('.video-duration')[0].text

        # Here we make second request
        second_soup = make_request(href, mobile=True)
        embed = second_soup.select('div#html5_vid a')[0].get('href')
        desc = ''

        views = second_soup.select('div.video-details-inside table tr')[1].select('td')[1].text.split()[0]
        categories = second_soup.select('div.video-details-inside table tr')[0].select('.links')[0].text.split(',')

        images = []
        for i in range(1, 17):
            images.append(image.split('.jpg')[0][:-5] + '_0%02dm' % i + '.jpg')

        save_document(sender, title, href, images, embed, desc, duration, views, categories)


@two.connect
def processsTwo(sender):
    soup = make_request(sender.url)
    itemList = soup.select('#miniatura')
    for item in itemList:
        href = urlparse.urljoin(sender.url, item.find(class_='frame').get('href'))
        duration = item.select('span#title2 span.thumbtime')[0].text.strip()
        views = item.select('span#title2 span.thumbviews')[0].text.strip('Views: ')
        desc = ''

        # Dig deeper
        second_soup = make_request(href)
        title = second_soup.select('#video_text h3')[0].text
        categories = filter(None, [anchor.text for anchor in second_soup.select('#tags a')[1:]])

        image = item.find('img', class_='lazy').get('data-original')
        images = []
        images.append(image)
        for i in range(2, 9):
            images.append(image.replace('flv-1', 'flv-%s' % i))

        mobile_href = urlparse.urljoin(sender.mobile_url, item.find(class_='frame').get('href'))

        mobile_soup = make_request(mobile_href)

        embed = mobile_soup.select('a.preview_thumb')[0].get('href')

        save_document(sender, title, href, images, embed, desc, duration, views, categories)
