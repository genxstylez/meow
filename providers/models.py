# -*- coding: utf-8 -*-
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    mobile_url = models.URLField(max_length=100)
    codename = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    def get_contents(self):
        if self.codename == 'RT':
            from providers.signals import one
            one.send(self)
        if self.codename == 'YJ':
            from providers.signals import two
            two.send(self)

    @models.permalink
    def get_absolute_url(self):
        return ('provider', [self.id])
