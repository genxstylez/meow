# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from documents.models import Document


def document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    return render(request, 'document.html', {'document': document})
