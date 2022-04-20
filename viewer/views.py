from django.http import HttpResponse
from django.shortcuts import render


def hello(request, s):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s}World!')
