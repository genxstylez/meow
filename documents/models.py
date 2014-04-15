# -*- coding: utf-8 -*-
from django.db import models

from providers.models import Provider


class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('category', [self.id])


class Document(models.Model):
    provider = models.ForeignKey(Provider)
    categories = models.ManyToManyField(Category, related_name='docs')
    title = models.CharField(max_length=300)
    href = models.CharField('Related url', max_length=255, unique=True)
    image = models.URLField(max_length=300)
    views = models.PositiveIntegerField(default=0)
    embed = models.CharField(max_length=300)
    desc = models.CharField(max_length=300, blank=True)
    duration = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return '%s%s' % (self.provider.url, self.href.lstrip('/'))

    @models.permalink
    def get_absolute_url(self):
        return ('document', [self.id])
