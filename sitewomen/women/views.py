from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Women app index page")


##def categories(request):
##    return HttpResponse('<h1>Categories page</h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories page</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Categories page</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Categories page</h1><p>archive year: {year}</p>')