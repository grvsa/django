from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("Women app index page")


def categories(request):
    return HttpResponse('<h1>Categories page</h1>')
