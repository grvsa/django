from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponse("Women app index page")


##def categories(request):
##    return HttpResponse('<h1>Categories page</h1>')

def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories page</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    else:
        print('GET EMPTY')

    if request.POST:
        print(request.POST)
    else:
        print('POST EMPTY')

    return HttpResponse(f'<h1>Categories page</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2024:

        # raise Http404()
        # return redirect('/') #на адрес главной страницы с кодом 302 - временно
        # return redirect('/', permanent=True) # на адрес главной страницы с кодом 301 - постоянно
        # return redirect(index, permanent=True) #так тоже можно
        # return redirect('home') #по имени страницы
        # return redirect('cats', 'music')
        uri = reverse('cats', args=['music',])
        # return redirect(uri)
        # return HttpResponseRedirect('home')
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f'<h1>Categories page</h1><p>archive year: {year}</p>')


def page_not_found(request, exception):
    print(exception)
    return HttpResponseNotFound(f'<h1>Requested page is not found</h1><p>Try to change URL adress</p>')