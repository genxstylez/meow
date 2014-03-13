from django.conf.urls import patterns, include, url

from django.contrib import admin
from sitemap import sitemaps

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'meow.views.index', name='index'),
    url(r'^document/(?P<document_id>\d+)/$', 'documents.views.document', name='document'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)
