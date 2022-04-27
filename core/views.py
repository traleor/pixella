from django.conf import settings
from django.shortcuts import render
from django.template.response import TemplateResponse


def index(request):
    frontend_url = ""
    return TemplateResponse(
        request,
        "index.html",
        {"frontend_url": frontend_url},
    )