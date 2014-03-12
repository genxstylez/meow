# -*- coding: utf-8 -*-
from django.db import models

from providers.models import Provider


class Document(models.Model):
    provider = models.ForeignKey(Provider)
    title = models.CharField(max_length=300)
    href = models.CharField('Related url', max_length=500, unique=True)
    image = models.URLField(max_length=300)
    hits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return '%s%s' % (self.provider.url, self.href.lstrip('/'))

    @models.permalink
    def get_absolute_url(self):
        return ('document', [self.id])
        