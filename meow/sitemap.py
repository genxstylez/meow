# -*- coding: utf-8 -*-

from django.contrib.sitemaps import GenericSitemap
from documents.models import Document

documents = {
    'queryset': Document.objects.all(),
    'date_field': 'last_modified'
}

sitemaps = {
    'videos': GenericSitemap(documents, priority=1, changefreq='daily'),
}
