from django.conf.urls import patterns, include, url

from django.contrib import admin
from sitemap import sitemaps

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'meow.views.index', name='index'),
    url(r'^document/(?P<document_id>\d+)/$', 'documents.views.document', name='document'),
    url(r'^document/hits/(?P<document_id>\d+)/$', 'documents.views.hits', name='document-hits'),
    url(r'^category/(?P<category_id>\d+)/$', 'documents.views.category', name='category'),
    url(r'^provider/(?P<provider_id>\d+)/$', 'providers.views.provider', name='provider'),
    url(r'^meowadmin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
