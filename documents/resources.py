from __future__ import unicode_literals

import urlparse
from tastypie.resources import ModelResource, fields, ALL_WITH_RELATIONS
from documents.models import Category, Image, Document
from providers.signals import make_request


class ImageResource(ModelResource):

    class Meta:
        queryset = Image.objects.all()
        resource_name = 'images'


class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        allowed_methods = ['get']


class DocumentResource(ModelResource):
    categories = fields.ToManyField(CategoryResource, 'categories', full=True, null=True, blank=True)
    images = fields.ToManyField(ImageResource, 'images', full=True)
    embed = fields.CharField(attribute='embed', use_in='detail')

    class Meta:
        queryset = Document.objects.order_by('-last_modified', '-views')
        resource_name = 'documents'
        list_allowed_methods = ['get', ]
        detailed_allowed_methods = ['get', ]
        filtering = {
            'categories': ALL_WITH_RELATIONS,
        }

    def dehydrate_embed(self, bundle):
        embed = ''
        try:
            if bundle.obj.provider.codename == 'RT':
                soup = make_request(bundle.obj.href, mobile=True)
                embed = soup.select('div#html5_vid a')[0].get('href')
            elif bundle.obj.provider.codename == 'YJ':
                mobile_href = urlparse.urljoin(bundle.obj.provider.mobile_url, urlparse.urlparse(bundle.obj.href).path)
                mobile_soup = make_request(mobile_href)
                embed = mobile_soup.select('a.preview_thumb')[0].get('href')

        except IndexError:
            pass
        return embed
