# -*- coding: utf-8 -*-

from django.http import HttpResponse


def provider(request, provider_id):
    return HttpResponse(200)
