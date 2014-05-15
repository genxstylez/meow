# -*- coding: utf-8 -*-

from django.contrib import admin
from documents.models import Document, Category, Image


class CategoryAdmin(admin.ModelAdmin):
    pass


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('provider', 'title', 'href')


class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Document, DocumentsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
