from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'page_views/index.html', {})