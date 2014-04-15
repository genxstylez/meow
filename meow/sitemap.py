# -*- coding: utf-8 -*-

from django.contrib.sitemaps import GenericSitemap
from providers.models import Provider
from documents.models import Document, Category

documents = {
    'queryset': Document.objects.all(),
    'date_field': 'last_modified'
}

categories = {
    'queryset': Category.objects.all(),
    'date_field': 'created_at'
}

providers = {
    'queryset': Provider.objects.all(),
    'date_field': 'created_at'
}

sitemaps = {
    'videos': GenericSitemap(documents, priority=1, changefreq='daily'),
    'categories': GenericSitemap(categories, priority=0.8, changefreq='weekly'),
    'providers': GenericSitemap(providers, priority=0.5, changefreq='monthly')
}
