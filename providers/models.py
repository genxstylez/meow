# -*- coding: utf-8 -*-
from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    css_selector = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name
