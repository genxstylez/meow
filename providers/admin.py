# -*- coding: utf-8 -*-

from django.contrib import admin
from providers.models import Provider


class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'css_selector')

admin.site.register(Provider, ProvidersAdmin)
