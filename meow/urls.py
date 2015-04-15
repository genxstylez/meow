from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic import TemplateView
from sitemap import sitemaps
from tastypie.api import Api
from documents.resources import CategoryResource, ImageResource, DocumentResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CategoryResource())
v1_api.register(ImageResource())
v1_api.register(DocumentResource())

urlpatterns = patterns('',
                       # url(r'^$', 'meow.views.index', name='index'),
                       url(r'^$', TemplateView.as_view(template_name='app.html'), name='index'),
                       url(r'^document/(?P<document_id>\d+)/$', 'documents.views.document', name='document'),
                       url(r'^document/hits/(?P<document_id>\d+)/$', 'documents.views.hits', name='document-hits'),
                       url(r'^category/(?P<category_id>\d+)/$', 'documents.views.category', name='category'),
                       url(r'^provider/(?P<provider_id>\d+)/$', 'providers.views.provider', name='provider'),
                       url(r'^meowadmin/', include(admin.site.urls)),
                       url(r'^api/', include(v1_api.urls)),
                       (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
                       )
