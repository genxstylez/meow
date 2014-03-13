# -*- coding: utf-8 -*-

from django.contrib import admin
from documents.models import Document


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('provider', 'title', 'href')

admin.site.register(Document, DocumentsAdmin)
