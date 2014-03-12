# -*- coding: utf-8 -*-
from django.db import models

from providers.models import Provider


class Document(models.Model):
    provider = models.ForeignKey(Provider)
    title = models.CharField(max_length=300)
    rel_url = models.CharField('Related url', max_length=500, unique=True)
    content = models.CharField(max_length=3000)

    @property
    def url(self):
        return '%s%s' % (self.provider.url, self.rel_url)
