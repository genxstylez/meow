# -*- coding: utf-8 -*-

from django.contrib import admin
from documents.models import Document


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('provider', 'title', 'rel_url')

admin.site.register(Document, DocumentsAdmin)
