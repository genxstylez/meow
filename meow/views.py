# -*- coding: utf-8 -*-

from django.shortcuts import render

from documents.models import Document


def index(request):
    documents = Document.objects.order_by('hits')

    return render(request, 'index.html', {'documents': documents})
