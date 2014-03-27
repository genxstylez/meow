# -*- coding: utf-8 -*-
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    codename = models.CharField(max_length=2)

    def __unicode__(self):
        return self.name

    def get_contents(self):
        if self.codename == 'XH':
            from providers.signals import one
            one.send(self)
